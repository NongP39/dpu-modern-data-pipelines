select 
    dt,
    temp,
    feels_like,
    temp - feels_like as diff

from {{ref("temp_greater_than_25")}}
where feels_like is not null