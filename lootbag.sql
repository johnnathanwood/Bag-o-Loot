-- Sometimes needed when you want to delete rows from a table while preserving the table
-- DELETE FROM child;
-- DELETE FROM gift;

-- Makes sure the CASCADE works
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS child;
DROP TABLE IF EXISTS gift;


CREATE TABLE `child` (
    `childId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Name`    TEXT NOT NULL,
    `receiving`    BIT NOT NULL
);

CREATE TABLE `gift` (
    `giftId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Name`    TEXT NOT NULL,
    `delivered`    BIT NOT NULL,
    `childId`    INTEGER NOT NULL,
    FOREIGN KEY(`childId`)
    REFERENCES `child`(`childId`)
    ON DELETE cascade
);
INSERT INTO gift
SELECT NULL, 'LightSaber', 1 ,childId
FROM Child 
Where  Child.Name = 'Billy';

INSERT INTO gift
SELECT NULL, 'Doll', 1 , childId
FROM Child 
WHERE  Child.Name = 'Sussy';

INSERT INTO gift
Select null, 'Bike', 1 , childId
FROM Child 
WHERE  Child.Name = 'Maddie';

INSERT INTO Child VALUES (null, 'Sussy', 1);
INSERT INTO Child VALUES (null, 'Billy', 1);
INSERT INTO Child VALUES (null, 'Maddie', 1);  