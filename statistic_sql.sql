--select suburb,count(*) as cc from webonsite_onsiteorigin group by suburb order by cc desc
--select suburb,count(*) as cc from webonsite_onsiteorigin group by suburb order by suburb
--select * from webonsite_onsiteorigin where price between 700000 and 1600000 and unit_percentage<0.5 and income>100000 and remuneration>80000 order by suburb
select crawl_date,count(*) as cc from webonsite_onsiteorigin group by crawl_date