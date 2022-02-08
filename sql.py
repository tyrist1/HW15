# `'age_upon_outcome'` — возраст животного на момент прибытия в приют.
#  не выносим
# `'animal_id'` — идентификатор животного. не выносим
# отдельная таблица
# `'animal_type'` — тип животного.
#
# `'name'` — кличка. не выносим
# отдельная таблица
# `'breed'` — порода.
#  отдельная таблица
# `'color1', 'color2'` — цвет или сочетание цветов.
#
# `'date_of_birth'` — дата рождения. не выносим

# отдельная таблица
# `'outcome_subtype'` — программа, в которой участвует животное. (В Америке есть разные варианты программ для бездомных животных. Например, про SCRP из нашей таблицы можно прочесть [здесь](https://www.maddiesfund.org/austin-animal-services-stray-cat-return-program.htm).)
# `'outcome_type'` — что сейчас с животным.
# `'outcome_month'` — месяц прибытия.
# `'outcome_year'` — год прибытия.

import sqlite3

con = sqlite3.connect("animal.db")
cur = con.cursor()
query = """
    CREATE TABLE COLORS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT
    ,NAME VARCHAR(30))
    
"""

cur.execute(query)
con.close()
# ДОБАВИЛ ТАБЛИЦУ
import sqlite3

con = sqlite3.connect("animal.db")
cur = con.cursor()
query = """
    INSERT INTO COLORS(NAME)
    SELECT * FROM
    (select distinct rtrim(color1)
    from animals
    union
    select distinct rtrim(color2)
    from animals where color2 is not null)
"""

cur.execute(query)
con.close()
# ЗАПОЛНИЛ ЦВЕТАМИ, ЦВЕТА РАЗДЕЛИЛ И СОБРАЛ ВОЕДИНО
create table animals_colors(
    animal_id integer
    ,color_id integer
)
# sosdal table соед. цвета и животных

insert into animals_colors
select animals."index",
       COLORS.name
from animals
join COLORS on rtrim(animals.color1)=rtrim(COLORS.NAME);

insert into animals_colors
select animals."index",
       COLORS.name
from animals
join COLORS on rtrim(animals.color2)=rtrim(COLORS.NAME)
#  заполнили связь животных и цветов