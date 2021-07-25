import psycopg2

connection = psycopg2.connect(
    database="dfanc7ubadgs35",
    user="gozrobhbrwcfne",
    password="6bbec15c064964ebc7d1323e5f7f8cd11db194f67f49cd6f8ab4b42a60f0509f",
    host="ec2-54-220-170-192.eu-west-1.compute.amazonaws.com",
    port="5432"
)

cursor = connection.cursor()

# cursor.execute('''
#     DROP TABLE IF EXITS models, cars, owners, ownerscars CASCADE;
#     );
# ''')

cursor.execute('''
    CREATE TABLE models (
        id serial PRIMARY KEY,
        modelName varchar(255),
        range int
    );
''')

cursor.execute('''
    CREATE TABLE cars (
        id serial PRIMARY KEY,
        modelId int,
        plateNo varchar(255),
        FOREIGN KEY (modelId) REFERENCES models (id) 
    );
''')

cursor.execute('''
    CREATE TABLE owners (
        id serial PRIMARY KEY,
        fullName varchar(255),
        personalId int
    );
''')

cursor.execute('''
    CREATE TABLE ownersCars (
        carId int,
        ownerId int,
        FOREIGN KEY (carId) REFERENCES cars (id), 
        FOREIGN KEY (ownerId) REFERENCES owners (id) 
    );
''')

cursor.execute('''
    INSERT INTO models (modelName, range)
    VALUES
        ('Tesla A', 20),
        ('Tesla A', 20),
        ('Tesla A', 20);
        
    INSERT INTO owners (fullName, personalId)
    VALUES
        ('John A', 10),
        ('John B', 20),
        ('John C', 30),
        ('John D', 40),
        ('John E', 50),
        ('John F', 60),
        ('John G', 70),
        ('John H', 80),
        ('John I', 90),
        ('John J', 100);
        
    INSERT INTO cars (modelId, plateNo)
    VALUES
        (1, 'A-12345'),
        (2, 'B-12345'),
        (3, 'C-12345'),
        (1, 'D-12345'),
        (2, 'E-12345'),
        (3, 'F-12345'),
        (1, 'G-12345'),
        (2, 'H-12345'),
        (3, 'I-12345'),
        (1, 'J-12345'),
        (2, 'K-12345'),
        (3, 'L-12345'),
        (1, 'M-12345'),
        (2, 'N-12345'),
        (3, 'O-12345');
        
    INSERT INTO ownersCars (carId, ownerId)
    VALUES  
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 1),
        (12, 2),
        (13, 3),
        (14, 4),
        (15, 5);
''')

connection.commit()

