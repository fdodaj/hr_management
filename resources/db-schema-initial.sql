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
  "created_at" timestamp,
  "deleted" boolean
);

CREATE TABLE "role" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "description" varchar
);

CREATE TABLE "department" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "description" varchar,
  "department_leader" varchar,
  "parent_department" int
);

CREATE TABLE "request_permisson" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "description" varchar,
  "from_date" date,
  "to_date" date,
  "business_days" int,
  "request_type" varchar,
  "request_status" boolean
);

CREATE TABLE "holiday" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "description" varchar,
  "date" date,
  "is_active" boolean
);

ALTER TABLE "user" ADD FOREIGN KEY ("id") REFERENCES "role" ("id");

ALTER TABLE "user" ADD FOREIGN KEY ("id") REFERENCES "department" ("id");

ALTER TABLE "request_permisson" ADD FOREIGN KEY ("id") REFERENCES "user" ("id");

ALTER TABLE "department" ADD FOREIGN KEY ("parent_department") REFERENCES "department" ("id");
