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
SELECT p.name, a.name, a.species
FROM people p 
JOIN people_animals pa ON p.person_id = pa.owner_id
JOIN animals a ON pa.pet_id = a.animal_id
WHERE p.name = 'bessie'
AND a.animal_id NOT IN (
    SELECT pa.pet_id
    FROM people_animals pa
    JOIN people p_sub ON pa.owner_id = p_sub.person_id
    JOIN animals a ON pa.pet_id = a.animal_id
    WHERE p_sub.name != 'bessie'
);
"""
