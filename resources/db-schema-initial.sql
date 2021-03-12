CREATE TABLE "user" (
  "id" SERIAL PRIMARY KEY,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "password" varchar,
  "phone_number" varchar,
  "birthday" date,
  "address" varchar,
  "gender" varchar,
  "hire_date" date,
  "paid_time_off" int,
  "user_status" varchar,
  "date_created" timestamp,
  "date_deleted" timestamp,
  "is_deleted" boolean,
  "role" varchar
);

CREATE TABLE "role" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "description" varchar,
  "date_created" timestamp,
  "date_deleted" timestamp,
  "is_deleted" boolean
);

CREATE TABLE "department" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "description" varchar,
  "department_leader" varchar,
  "parent_department" int,
  "date_created" timestamp,
  "date_deleted" timestamp,
  "is_deleted" boolean
);

CREATE TABLE "request_permisson" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "reason" varchar,
  "from_date" date,
  "to_date" date,
  "business_days" int,
  "request_type" varchar,
  "request_status" varchar,
  "date_created" timestamp,
  "date_deleted" timestamp,
  "is_deleted" boolean
);

CREATE TABLE "holiday" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "description" varchar,
  "date" date,
  "is_active" boolean,
  "date_created" timestamp,
  "date_deleted" timestamp,
  "is_deleted" boolean
);

ALTER TABLE "user" ADD FOREIGN KEY ("id") REFERENCES "role" ("id");

ALTER TABLE "user" ADD FOREIGN KEY ("id") REFERENCES "department" ("id");

ALTER TABLE "request_permisson" ADD FOREIGN KEY ("id") REFERENCES "user" ("id");

ALTER TABLE "department" ADD FOREIGN KEY ("parent_department") REFERENCES "department" ("id");
