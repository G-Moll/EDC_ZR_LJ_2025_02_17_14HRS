CREATE DATABASE Editorial;
USER Editorial;

CREATE TABLE Branches(
    id INT( 11 ) UNSIGNED N
    OT NULL PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR( 8 ) NOT NULL,
    address VARCHAR( 255 ) NOT NULL,
    phone VARCHAR( 15 ) NOT NULL
);

CREATE TABLE Employees(
    id INT( 11 ) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    rfc VARCHAR( 18 ) NOT NULL,
    name VARCHAR( 50 ) NOT NULL,
    lastname VARCHAR( 80 ) NOT NULL,
    phone VARCHAR( 15 ) NOT NULL,

    branch_id INT( 11 ) UNSIGNED NOT NULL,

    FOREIGN KEY( branch_id ) REFERENCES Branches( id )
);
