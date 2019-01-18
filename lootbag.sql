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
    `delivered`    TEXT NOT NULL,
    `childId`    INTEGER NOT NULL,
    FOREIGN KEY(`childId`)
    REFERENCES `child`(`childId`)
    ON DELETE cascade
);