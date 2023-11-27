CREATE TABLE dispositivos (
    id          INTEGER PRIMARY KEY,
    dispositivo VARCHAR(100),
    led         INTEGER CHECK (led >= 0 AND led <= 1),
    sensor      INTEGER DEFAULT 0
);

INSERT INTO dispositivos (id, dispositivo, led, sensor)
VALUES (1, 'ESP32', 0, 0);

SELECT * FROM dispositivos;
