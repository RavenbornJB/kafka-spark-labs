CREATE KEYSPACE IF NOT EXISTS lab WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1};

USE lab;

-- a transaction is fully identifiable via uid (id of sender), rid (id of receiver) and date
-- now we just add partition or clustering keys based on needed requests

CREATE TABLE user_fraudulent (  -- only fraudulent transastions make their way here (via client filtering)
    sid text,
    rid text,
    amount float,
    transaction_date date,
    PRIMARY KEY (sid, transaction_date, rid)
) WITH CLUSTERING ORDER BY (transaction_date ASC, rid ASC);

-- SELECT * FROM user_fraudulent WHERE sid='qwer';

CREATE TABLE user_highest (
    sid text,
    rid text,
    amount float,
    transaction_date date,
    fraud boolean,
    PRIMARY KEY (sid, amount, transaction_date, rid)
) WITH CLUSTERING ORDER BY (amount DESC, transaction_date ASC, rid ASC);

-- SELECT * FROM user_highest WHERE sid='qwer' LIMIT 3;

CREATE TABLE user_date_sum (
    rid text,
    sid text,
    amount float,
    transaction_date date,
    fraud boolean,
    PRIMARY KEY (rid, transaction_date, sid)
) WITH CLUSTERING ORDER BY (transaction_date ASC, sid ASC);

-- SELECT SUM(amount) FROM user_date_sum WHERE rid='qwer' AND transaction_date>='2011-02-05' AND transaction_date<='2011-02-06';
