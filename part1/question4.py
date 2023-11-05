import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """
select name, species, age
from animals 
where animal_id not in (select pet_id from people_animals)
"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """
select count(*)
from people_animals pa 
inner join people p on pa.owner_id = p.person_id
inner join animals a on pa.pet_id = a.animal_id
where a.age > p.age 
"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 
SELECT people.name, pet.name, pet.species
FROM people as p
JOIN animals as a on p.person_id = a.owner_id
WHERE person.name = 'bessie'
AND NOT EXISTS (
    SELECT p.name
    FROM people_animals pa
    INNER JOIN animals a on pa.pet_id = a.animal_id
    INNER JOIN people as p on pa.owner_id = p.person_id
    WHERE pa.pet_id = a.animal_id
    AND pa.owner_id != p.person_id
"""