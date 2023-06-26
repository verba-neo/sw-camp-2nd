from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'#{self.id}: {self.name}'
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f'#{self.id}: {self.title}'


# class ActorMovie(models.Model):
#     actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


if __name__ == '__main__':

    a1 = Actor.objects.get(pk=1)
    a2 = Actor.objects.get(pk=2)
    a3 = Actor.objects.get(pk=3)
    a4 = Actor.objects.get(pk=4)

    m1 = Movie.objects.get(pk=1)
    m2 = Movie.objects.get(pk=2)


    # M:N 관계 추가
    m1.actors.add(a1)
    m1.actors.add(a2, a3)

    # Actor는 명시적인 Attribute 없음 => _set
    a1.movie_set.add(m2)
    a4.movie_set.add(m2)

    m2.actors.add(a2)
    # 기존의 M:N 관계 삭제
    m2.actors.remove(a2)

    # 배우의 필모
    a1.movie_set.all()
    # 영화의 출연진
    m1.actors.all()