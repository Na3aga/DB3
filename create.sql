--сутність City
--ключем є назва міста

CREATE TABLE City (
    city VARCHAR(40) NOT NULL PRIMARY KEY,
    region VARCHAR(40) NOT NULL ,
    state_code VARCHAR(4),
    country_code VARCHAR(4) NOT NULL
    );

--сутність Startup
--ключем є назва, вона унфікальна

CREATE TABLE Startup(
    name VARCHAR(50) NOT NULL PRIMARY KEY,
    city VARCHAR(40) NOT NULL REFERENCES City(city),
    market VARCHAR(40) NOT NULL ,
    total_funding INTEGER NOT NULL CHECK ( total_funding > 0 ),
    website VARCHAR(255) NOT NULL
    );

--сутність Investment
--ключем є ідентифікатор, можна було б виористати назву стартапу, адже в даному датасеті інвестиції трапляються один раз

CREATE TABLE Investment (
    invstid INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL REFERENCES Startup(name),
    seed INTEGER NOT NULL,
    venture INTEGER NOT NULL
);


ALTER TABLE Investment
  ADD (
    CONSTRAINT invst_pk PRIMARY KEY (invstid)
  );

CREATE SEQUENCE invst_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER invst_bir
BEFORE INSERT ON Investment
FOR EACH ROW

BEGIN
  SELECT invst_seq.NEXTVAL
  INTO   :new.invstid
  FROM   dual;
END;
