-- solvesql: 작품이 없는 작가 찾기

select artist_id, name
from artists
where death_year is not null
  and artist_id not in (
    select artist_id
    from artworks_artists
  )