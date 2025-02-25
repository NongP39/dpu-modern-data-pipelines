select 
    temp

from {{ source("dpu","weathers") }}
where temp > 25