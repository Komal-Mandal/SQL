# interview-preparation

# SQL 

# 1. Introduction

SQL (Structured Query Language) is a powerful tool used to store, retrieve, and manage data in relational databases. It is widely utilized in Data Science and Software Development to work with structured data, perform calculations, and organize information efficiently. Learning SQL helps in handling large datasets, optimizing performance, and making better data-driven decisions.

# 2. Database Keys

Keys help in identifying and organizing records in a database:

# Primary Key: 

A unique identifier for each record in a table (e.g., Student_ID in a Student table). Only one per table.

# Foreign Key: 

A field in one table that refers to the Primary Key of another table, establishing relationships (e.g., Course_ID in the Enrollment table referencing Course_ID in the Courses table).

# Candidate Key: 

A set of columns that can uniquely identify records. One of them becomes the Primary Key (e.g., Email and Student_ID in a Student table).

# Composite Key: 

A key made up of two or more columns that together ensure uniqueness (e.g., (Student_ID, Course_ID) in an Enrollment table).

# Super Key:

A set of columns that uniquely identify a record but may have extra unnecessary attributes (e.g., (Student_ID, Email, Phone)).

# Alternate Key:

 A Candidate Key that is not chosen as the Primary Key (e.g., If Student_ID is the Primary Key, Email is an Alternate Key).


# 3. Types of SQL Commands

SQL is divided into different types based on functionality:

1.DDL (Data Definition Language) – Defines the database structure (e.g., CREATE, ALTER, DROP).

2.DML (Data Manipulation Language) – Modifies database records (e.g., INSERT, UPDATE, DELETE).

3.DCL (Data Control Language) – Manages user permissions (e.g., GRANT, REVOKE).

4.TCL (Transaction Control Language) – Handles transactions (e.g., COMMIT, ROLLBACK).

5.DQL (Data Query Language) – Fetches data from tables (e.g., SELECT).

# 4. GROUP BY Clause

The GROUP BY clause groups rows with the same values and applies functions like COUNT, SUM, or AVG to summarize data.

# 5. CASE Statement

The CASE statement allows conditional logic in SQL queries, helping in decision-making based on specific values.

# 6. SQL Joins

Joins combine data from multiple tables based on common fields:

1.INNER JOIN – Returns matching records from both tables.

2.LEFT JOIN – Returns all records from the left table and matching records from the right table.

3.RIGHT JOIN – Returns all records from the right table and matching records from the left table.

4.FULL JOIN – Returns all records from both tables.

5.CROSS JOIN – Matches every row from one table with all rows from another.

# 7. Subquery

A subquery is a query inside another query, used to fetch data required for the main query.

# 8. Indexing

An index improves query speed by allowing the database to locate records faster.

# 9. Views

A view is a saved SQL query that acts as a virtual table, simplifying data access and security.

# 10. ACID Properties

ACID ensures reliable database transactions:

1.Atomicity – A transaction is either fully completed or not at all.

2.Consistency – The database remains in a valid state before and after transactions.

3.Isolation – Transactions do not interfere with each other.

4.Durability – Completed transactions are permanently stored.

# 11. Normalization

Normalization eliminates redundancy and ensures efficient data storage.

1.1NF (First Normal Form) – Remove duplicate values and ensure atomicity.

2.2NF (Second Normal Form) – Remove partial dependency (every non-key column should depend on the whole primary key).

3.3NF (Third Normal Form) – Remove transitive dependency (non-key columns should not depend on other non-key columns).

4.BCNF (Boyce-Codd Normal Form) – Stronger 3NF where every determinant is a candidate key.

5.4NF (Fourth Normal Form) – Remove multivalued dependencies.

# 12. Triggers

A trigger is an automatic action executed when specific changes occur in the database, helping maintain consistency.

# 13. Constraints

A constraint is a rule that ensures data integrity and reliability:

1.PRIMARY KEY – Ensures unique values for each record.

2.FOREIGN KEY – Maintains relationships between tables.

3.NOT NULL – Prevents empty values.

4.UNIQUE – Ensures all values in a column are different.

5.CHECK – Restricts values (e.g., age must be greater than 0).

6.DEFAULT – Assigns a default value if none is provided.

# 14. Alias

An alias is a temporary name assigned to a table or column for the duration of a query, improving readability.

# 15. Difference Between DROP vs DELETE

DROP: A DDL command that completely removes a table or database, including its structure.

DELETE: A DML command that removes specific rows from a table based on a condition.

# 16. Difference Between BETWEEN and IN Operators

BETWEEN: Used to filter values within a range (inclusive).

IN: Used to filter specific values from a given list.

# 17. AUTO_INCREMENT

AUTO_INCREMENT automatically generates unique numbers for a column, commonly used for Primary Keys.

# 18. UNION, MINUS, and INTERSECT Operators

1.UNION: Combines results from two queries and removes duplicates.

2.MINUS: Returns rows from the first query that are not in the second query.

3.INTERSECT: Returns rows that are common to both queries.

# 19. Functions in SQL

Functions perform specific tasks and return results efficiently.

# 20. Difference Between UNION and UNION ALL

UNION: Combines results of multiple SELECT queries and removes duplicate rows.

UNION ALL: Combines results of multiple SELECT queries, including duplicates.
