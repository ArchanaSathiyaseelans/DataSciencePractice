use moviesdb;
select * from movies where industry ="bollywood";

select title, industry from moviesdb.movies;

select count(*) from movies where industry ="hollywood";

select distinct industry from movies;

select * from movies where title like "%THOR%";

select * from movies where studio="";

select * from movies where imdb_rating >= 9;

select * from movies where imdb_rating >= 6 and imdb_rating <=8;

select * from movies where imdb_rating between 6 and 8;

select * from movies where release_year=2022;

select * from movies where release_year=2022 or  release_year=2019 or  release_year=2018;

select * from movies where release_year in (2022,2019,2018)

select * from movies where studio in ("Marvel Studio", "Zee studios");

select * from movies where  industry = "bollywood" order by imdb_rating desc limit 5;

select * from movies where  industry = "hollywood" order by imdb_rating desc limit 5 offset 4;

select max(imdb_rating) from movies where  industry = "bollywood";

select round(avg(imdb_rating),2) from movies where  industry = "bollywood";

select round(avg(imdb_rating),2)  as avg_rating from movies where studio="Marvel Studios";

select min(imdb_rating) as min_rating, 
max(imdb_rating) as max_rating,
round(avg(imdb_rating), 2) as avg_rating
from movies where studio="Marvel Studios";


select industry, count(industry) as cnt, avg(imdb_rating) as avg_rating from movies group by industry;

select movies.movie_id, title, budget, revenue, currency, unit 
from movies 
inner join financials 
on movies.movie_id=financials.movie_id;

select m.movie_id, title, budget, revenue, currency, unit 
from movies m
inner join financials  f
on m.movie_id=f.movie_id;


select m.movie_id, title, budget, revenue, currency, unit 
from movies m
left join financials  f
on m.movie_id=f.movie_id;

select f.movie_id, title, budget, revenue, currency, unit 
from movies m
right join financials  f
on m.movie_id=f.movie_id;

select m.movie_id, title, budget, revenue, currency, unit 
from movies m left join financials  f on m.movie_id=f.movie_id

union

select f.movie_id, title, budget, revenue, currency, unit 
from movies m right join financials  f on m.movie_id=f.movie_id;

select f.movie_id, title, budget, revenue, currency, unit 
from movies m right outer join financials  f on m.movie_id=f.movie_id;

select movie_id, title, budget, revenue, currency, unit 
from movies m right join financials  f using (movie_id)

select movie_id, title, budget, revenue, currency, unit 
from movies m left join financials  f using (movie_id);


