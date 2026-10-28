"""Pruebas del arranque conservador sin usar motores ni servicios reales."""

from pathlib import Path
import os
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "modules/06_apis_datos_eventos/start_services.sh"


class StartServicesTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.tmp = Path(self.directory.name)
        self.log = self.tmp / "commands.log"
        stub = """#!/bin/bash
printf '%s %s\\n' "${0##*/}" "$*" >> "$MOTOR_TEST_LOG"
if [[ "$1" == info && "${FAIL_INFO:-0}" == 1 ]]; then exit 1; fi
if [[ "$1 $2" == 'compose version' && "${FAIL_COMPOSE:-0}" == 1 ]]; then exit 1; fi
if [[ "$1" == compose && "$*" == *config && "${FAIL_CONFIG:-0}" == 1 ]]; then exit 1; fi
exit 0
"""
        for motor in ("podman", "docker"):
            path = self.tmp / motor
            path.write_text(stub, encoding="utf-8")
            path.chmod(0o700)
        self.env = dict(os.environ, PATH=f"{self.tmp}:{os.environ['PATH']}", MOTOR_TEST_LOG=str(self.log))

    def run_script(self, *args, **extra):
        return subprocess.run(
            ["bash", str(SCRIPT), *args], cwd=ROOT,
            env=dict(self.env, **extra), text=True, capture_output=True,
        )

    def test_default_plan_does_not_call_motor(self):
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Motor: podman", result.stdout)
        self.assertFalse(self.log.exists())

    def test_docker_plan_does_not_call_motor(self):
        result = self.run_script("--motor", "docker")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Motor: docker", result.stdout)
        self.assertFalse(self.log.exists())

    def test_invalid_arguments_fail_without_calling_motor(self):
        for args in (("--motor",), ("--motor", "other"), ("--unknown",)):
            with self.subTest(args=args):
                self.assertEqual(self.run_script(*args).returncode, 2)
        self.assertFalse(self.log.exists())

    def test_apply_checks_before_starting_both_motors(self):
        for motor in ("podman", "docker"):
            with self.subTest(motor=motor):
                self.log.unlink(missing_ok=True)
                result = self.run_script("--motor", motor, "--apply")
                self.assertEqual(result.returncode, 0, result.stderr)
                lines = self.log.read_text(encoding="utf-8").splitlines()
                self.assertEqual(len(lines), 5)
                self.assertEqual(lines[0], f"{motor} info")
                self.assertEqual(lines[1], f"{motor} compose version")
                self.assertTrue(lines[2].endswith("compose.yml config"))
                self.assertTrue(lines[3].endswith("compose.yml up -d postgres"))
                self.assertEqual(lines[4], f"{motor} ps --filter name=librereserva")

    def test_failed_prerequisite_does_not_start_services(self):
        for flag in ("FAIL_INFO", "FAIL_COMPOSE", "FAIL_CONFIG"):
            with self.subTest(flag=flag):
                self.log.unlink(missing_ok=True)
                result = self.run_script("--apply", **{flag: "1"})
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn("up -d", self.log.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
