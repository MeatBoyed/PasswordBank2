# Database Architecture

# Master Account

Master Account table contains fields; Username, Email and Password. All of which are compulsory.

```sql
CREATE TABLE masteraccount (
	username VARCHAR(225) PRIMARY KEY NOT NULL,
	email email NOT NULL,
	password CHAR(64) NOT NULL
);
```

Email field is tied to a Postgres DOMAIN to check that entered email is valid. [More Info](https://dba.stackexchange.com/questions/68266/what-is-the-best-way-to-store-an-email-address-in-postgresql)

Password is stored as 64 length Character string, because the Hashed Hex value of the password will always result in a 64 length Character string.

# Accounts

Accounts table contains fields; ID, Sitename, URL, Email and Password. URL is an optional field.

```sql
CREATE TABLE accounts (
	id BIGSERIAL PRIMARY KEY NOT NULL,
	sitename VARCHAR(225) NOT NULL,
	url TEXT,
	email email NOT NULL,
	password TEXT NOT NULL
)
```

All passwords saved to Accounts are encrypted.