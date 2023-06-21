from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='THIS IS DEFAULT CONTENT')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'#{self.pk}: {self.title}'


class Comment(models.Model):
    content = models.CharField(max_length=200)
    #                   FK      관계모델, 게시글 삭제시 => 댓글 모두 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE)



# 이 파일이 직접 실행 되었을 때만 실행할 코드
# 직접 실행 => $ python board/models.py
if __name__ == '__main__':
    print('--------------- This is board model ---------------')
    a1 = Article.objects.create(title='저녁메뉴', content='추천받는다')
    a2 = Article.objects.create(title='끝말잇기', content='텀블러')

    c1 = Comment()
    c1.article = a1
    c1.content = '치킨'
    c1.save()

    c2 = Comment.objects.create(article=a1, content='샐러드')
    c3 = Comment.objects.create(article=a1, content='제육볶음')

    c4 = Comment.objects.create(article=a2, content='러시아')
    c5 = Comment.objects.create(article=a2, content='아시아')
    c6 = Comment.objects.create(article=a2, content='아프리카')

    # c4 댓글의 내용은?
    c4.content
    # c4 댓글이 달린 게시글은?
    c4.article
    # c4 댓글이 달린 게시글의 제목은?
    c4.article.title
    # c4 댓글이 달린 게시글의 내용은?
    c4.article.content

    # a1 게시글에 달린 모든 댓글들? (default: 종속모델명_set)
    a1.comment_set.all()

    # a1 게시글에 달린 모든 댓글들의 내용을 출력하려면?
    for comment in a1.comment_set.all():
        print(comment.content)
        
    # c5가 달린 게시글에 달린 모든 댓글들의 내용을 출력하려면?
    for c in c5.article.comment_set.all():
        print(c.content)