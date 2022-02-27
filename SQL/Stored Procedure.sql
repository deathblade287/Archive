
declare @nm nvarchar(50)
declare @ag int
set @nm = 'Ishan'
set @ag=19
print @ag
print @nm

select * from players where age > @ag and name=@nm

create procedure nameage
as
begin
	select * from players where age>32
end

nameage

create proc nameageparam
@ag int
as
begin
	select * from players where age > @ag
end

nameageparam 'Virat'

sp_helptext nameageparam

drop procedure nameageparam


create proc playersagecountry
@ag int, @ctr nvarchar(50)
as
begin
	select * from players where age > @ag and country=@ctr
end

playersagecountry India,32

alter proc playersagecountry
@ag int
as
begin
	select * from players where age > @ag
end

playersagecountry 32