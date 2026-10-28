CREATE EXTENSION IF NOT EXISTS btree_gist;

CREATE TABLE IF NOT EXISTS reservas (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    recurso text NOT NULL,
    inicio timestamptz NOT NULL,
    fin timestamptz NOT NULL,
    CONSTRAINT reservas_intervalo_valido CHECK (fin > inicio),
    CONSTRAINT reservas_sin_solapamiento
        EXCLUDE USING gist (
            recurso WITH =,
            tstzrange(inicio, fin, '[)') WITH &&
        )
);
