# Database

## events

| param      | type          | option   |
| ---------- | ------------- | -------- |
| id         | BIGINT        | pk       |
| title      | VARCHAR(45)   | NOT NULL |
| owner      | VARCHAR(45)   | NOT NULL |
| url        | VARCHAR(2083) |
| note       | VARCHAR(1000) |
| date       | DATETIME      | NOT NULL |
| delete_key | VARCHAR(45)   | NOT NULL |
| updated_at | TIMESTAMP     | NOT NULL |
| created_at | TIMESTAMP     | NOT NULL |
