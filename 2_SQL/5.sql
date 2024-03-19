--1no
select * from cd.facilities;

--2no
select * from cd.facilities;
select name,membercost
from cd.facilities
limit 4;

--3no
select * from cd.facilities
where membercost > 0
limit 5;

--4no
select facid,name,membercost,monthlymaintenance
from cd.facilities
where membercost > 0 and
membercost <(monthlymaintenance/50.0);

--5no
select * from cd.facilities
where name like '%Tennis%';

--6no
select * from cd.facilities
where facid in (1,5);

--7no
select memid,surname,firstname,joindate 
from cd.members
where joindate >='2012-09-01';

--8 no
select DISTINCT surname from cd.members
order by surname
limit 10;

select surname from cd.members
group by surname
order by surname
limit 10;

--9 no
select joindate from cd.members
order by joindate desc
limit 1;

select min(joindate)
from cd.members;

--10 no
select count(*) from cd.facilities
where guestcost>=10;

--11 no
select facid ,sum(slots) as total_slots
from cd.bookings
where starttime >= '2012-09-01' and
starttime <= '2012-10-01'
group by facid 
order by sum(slots);

--12 no
select facid,sum(slots) as total_slots
from cd.bookings
group by facid
having sum(slots)>1000
order by sum(slots);

--13 no
select cd.bookings.starttime,cd.facilities.name
from cd.facilities
inner join cd.bookings
on cd.facilities.facid=cd.bookings.facid
where cd.facilities.name in ('Tennis Court 1','Tennis Court 2');

--14 no
select * from cd.members;
select * from cd.bookings;
select count(starttime) from cd.bookings
where memid in (select cd.members.memid from cd.members
			   where firstname='David' and surname='Farrell');
			   
select * from cd.bookings
inner join cd.members ON
cd.members.memid=cd.bookings.memid
where cd.members.firstname='David'
and cd.members.surname='Farrell';

