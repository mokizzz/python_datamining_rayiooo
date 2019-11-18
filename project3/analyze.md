### 1.1 问题内容足够吸引人

* word_vectors_64d
* topic_vectors_64d
* question_info_0926
* invite_info_0926



### 1.2 问题的回答数很多

* question_info_0926
* answer_info_0926 √

统计每个问题下回答的`回答数`、`优秀回答数`、`推荐回答数`、`收入圆桌回答数`、`包含图片回答数`、`包含视频回答数`、`回答内容字数平均数`、`回答总点赞数`、`回答总评论数`、`回答总收藏数`、`回答总感谢数`。

```mysql
# 插入列
alter table question_info_0926 add 回答数 int(11) default 0;
alter table question_info_0926 add 优秀回答数 int(11) default 0;
alter table question_info_0926 add 推荐回答数 int(11) default 0;
alter table question_info_0926 add 收入圆桌回答数 int(11) default 0;
alter table question_info_0926 add 包含图片回答数 int(11) default 0;
alter table question_info_0926 add 包含视频回答数 int(11) default 0;
alter table question_info_0926 add 回答内容字数平均数 int(11) default 0;
alter table question_info_0926 add 回答总点赞数 int(11) default 0;
alter table question_info_0926 add 回答总评论数 int(11) default 0;
alter table question_info_0926 add 回答总收藏数 int(11) default 0;
alter table question_info_0926 add 回答总感谢数 int(11) default 0;

# 设置好question.问题ID为主索引 answer.问题ID为索引 运行2min
create temporary table tmp as (select 问题ID, count(*) as 回答数 from answer_info_0926 group by 问题ID);
update question_info_0926 q, tmp set q.回答数 = tmp.回答数 where q.问题ID = tmp.问题ID;
drop table tmp;

create temporary table tmp as (select 问题ID, count(*) as 优秀回答数 from (select 问题ID from answer_info_0926 where 回答是否被标为优秀回答 = 1) as t group by 问题ID);
update question_info_0926 q, tmp set q.优秀回答数 = tmp.优秀回答数 where q.问题ID = tmp.问题ID;
drop table tmp;

create temporary table tmp as (select 问题ID, count(*) as 推荐回答数 from (select 问题ID from answer_info_0926 where 回答是否被推荐 = 1) as t group by 问题ID);
update question_info_0926 q, tmp set q.推荐回答数 = tmp.推荐回答数 where q.问题ID = tmp.问题ID;
drop table tmp;

# 废属性，因没有收入圆桌的回答
#create temporary table tmp as (select 问题ID, count(*) as 收入圆桌回答数 from (select 问题ID from answer_info_0926 where 回答是否被收入圆桌 = 1) as t group by 问题ID);
#update question_info_0926 q, tmp set q.收入圆桌回答数 = tmp.收入圆桌回答数 where q.问题ID = tmp.问题ID;
#drop table tmp;
# 包含图片回答数
create temporary table tmp as (select 问题ID, count(*) as 包含图片回答数 from (select 问题ID from answer_info_0926 where 回答是否包含图片 = 1) as t group by 问题ID);
update question_info_0926 q, tmp set q.包含图片回答数 = tmp.包含图片回答数 where q.问题ID = tmp.问题ID;
drop table tmp;
# 包含视频回答数
create temporary table tmp as (select 问题ID, count(*) as 包含视频回答数 from (select 问题ID from answer_info_0926 where 回答是否包含视频 = 1) as t group by 问题ID);
update question_info_0926 q, tmp set q.包含视频回答数 = tmp.包含视频回答数 where q.问题ID = tmp.问题ID;
drop table tmp;
# 回答内容字数平均数
create temporary table tmp as (
    select 问题ID, round(avg(回答的内容字数), 0) as 回答内容字数平均数 from answer_info_0926 group by 问题ID
);
update question_info_0926 q, tmp set q.回答内容字数平均数 = tmp.回答内容字数平均数 where q.问题ID = tmp.问题ID;
drop table tmp;
# 回答总点赞数
create temporary table tmp as (select 问题ID, sum(回答收到的点赞数) as 回答总点赞数 from answer_info_0926 group by 问题ID);
update question_info_0926 q, tmp set q.回答总点赞数 = tmp.回答总点赞数 where q.问题ID = tmp.问题ID;
drop table tmp;
# 回答总评论数
create temporary table tmp as (select 问题ID, sum(回答收到的评论数) as 回答总评论数 from answer_info_0926 group by 问题ID);
update question_info_0926 q, tmp set q.回答总评论数 = tmp.回答总评论数 where q.问题ID = tmp.问题ID;
drop table tmp;
# 回答总收藏数
create temporary table tmp as (select 问题ID, sum(回答收藏数) as 回答总收藏数 from answer_info_0926 group by 问题ID);
update question_info_0926 q, tmp set q.回答总收藏数 = tmp.回答总收藏数 where q.问题ID = tmp.问题ID;
drop table tmp;
# 回答总感谢数
create temporary table tmp as (select 问题ID, sum(回答收到的感谢数) as 回答总感谢数 from answer_info_0926 group by 问题ID);
update question_info_0926 q, tmp set q.回答总感谢数 = tmp.回答总感谢数 where q.问题ID = tmp.问题ID;
drop table tmp;
# 运行完成
```



### 2 人对问题足够感兴趣

* member_info_0926

train与test时计算每个人`关注话题命中数`、`感兴趣话题与此话题最大加权正余弦距离`。

### 3 人属于喜欢回答的类型

* member_info_0926

member表中的数据。

### 4 人的回答很优质

* answer_info_0926 √
* member_info_0926

统计每个人回答的`回答数`、`优秀回答数`、`推荐回答数`、`收入圆桌回答数`、`包含图片回答比例`、`包含视频回答比例`、`回答内容字数平均数`、`回答收到点赞平均数`、`回答收到取赞平均数`、`回答收到评论平均数`、`回答被收藏平均数`、`回答收到感谢平均数`、`回答被举报平均数`、`回答收到没有帮助平均数`、`回答收到反对平均数`。

```mysql
# 插入列
alter table member_info_0926 add 回答数 int(11) default 0;
alter table member_info_0926 add 优秀回答数 int(11) default 0;
alter table member_info_0926 add 推荐回答数 int(11) default 0;
#alter table member_info_0926 add 收入圆桌回答数 int(11) default 0;
alter table member_info_0926 add 包含图片回答比例 int(11) default 0;
alter table member_info_0926 add 包含视频回答比例 int(11) default 0;
alter table member_info_0926 add 回答内容字数平均数 int(11) default 0;
alter table member_info_0926 add 回答收到点赞平均数 int(11) default 0;
alter table member_info_0926 add 回答收到取赞平均数 int(11) default 0;
alter table member_info_0926 add 回答收到评论平均数 int(11) default 0;
alter table member_info_0926 add 回答被收藏平均数 int(11) default 0;
alter table member_info_0926 add 回答收到感谢平均数 int(11) default 0;
alter table member_info_0926 add 回答被举报平均数 int(11) default 0;
alter table member_info_0926 add 回答收到没有帮助平均数 int(11) default 0;
alter table member_info_0926 add 回答收到反对平均数 int(11) default 0;

# 回答数
create temporary table tmp as (select 用户ID, count(*) as 回答数 from answer_info_0926 group by 用户ID);
update member_info_0926 q, tmp set q.回答数 = tmp.回答数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 优秀回答数
create temporary table tmp as (select 用户ID, count(*) as 优秀回答数 from (select 用户ID from answer_info_0926 where 回答是否被标为优秀回答 = 1) as t group by 用户ID);
update member_info_0926 q, tmp set q.优秀回答数 = tmp.优秀回答数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 推荐回答数
create temporary table tmp as (select 用户ID, count(*) as 推荐回答数 from (select 用户ID from answer_info_0926 where 回答是否被推荐 = 1) as t group by 用户ID);
update member_info_0926 q, tmp set q.推荐回答数 = tmp.推荐回答数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 包含图片回答比例
create temporary table tmp as (select 用户ID, round(avg(回答是否包含图片) * 100, 0) as 包含图片回答比例 from answer_info_0926 group by 用户ID);
update member_info_0926 q, tmp set q.包含图片回答比例 = tmp.包含图片回答比例 where q.用户ID = tmp.用户ID;
drop table tmp;
# 包含视频回答比例
create temporary table tmp as (select 用户ID, round(avg(回答是否包含视频) * 100, 0) as 包含视频回答比例 from answer_info_0926 group by 用户ID);
update member_info_0926 q, tmp set q.包含视频回答比例 = tmp.包含视频回答比例 where q.用户ID = tmp.用户ID;
drop table tmp;
# 回答内容字数平均数
create temporary table tmp as (
    select 用户ID, round(avg(回答的内容字数), 0) as 回答内容字数平均数 from answer_info_0926 group by 用户ID
);
update member_info_0926 q, tmp set q.回答内容字数平均数 = tmp.回答内容字数平均数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 回答收到点赞平均数
create temporary table tmp as (
    select 用户ID, round(avg(回答收到的点赞数), 0) as 回答收到点赞平均数 from answer_info_0926 group by 用户ID
);
update member_info_0926 q, tmp set q.回答收到点赞平均数 = tmp.回答收到点赞平均数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 回答收到取赞平均数
create temporary table tmp as (
    select 用户ID, round(avg(回答收到的取赞数), 0) as 回答收到取赞平均数 from answer_info_0926 group by 用户ID
);
update member_info_0926 q, tmp set q.回答收到取赞平均数 = tmp.回答收到取赞平均数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 回答收到评论平均数
create temporary table tmp as (
    select 用户ID, round(avg(回答收到的评论数), 0) as 回答收到评论平均数 from answer_info_0926 group by 用户ID
);
update member_info_0926 q, tmp set q.回答收到评论平均数 = tmp.回答收到评论平均数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 回答被收藏平均数
create temporary table tmp as (
    select 用户ID, round(avg(回答收藏数), 0) as 回答被收藏平均数 from answer_info_0926 group by 用户ID
);
update member_info_0926 q, tmp set q.回答被收藏平均数 = tmp.回答被收藏平均数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 回答收到感谢平均数
create temporary table tmp as (
    select 用户ID, round(avg(回答收到的感谢数), 0) as 回答收到感谢平均数 from answer_info_0926 group by 用户ID
);
update member_info_0926 q, tmp set q.回答收到感谢平均数 = tmp.回答收到感谢平均数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 回答被举报平均数
create temporary table tmp as (
    select 用户ID, round(avg(回答收到的被举报数), 0) as 回答被举报平均数 from answer_info_0926 group by 用户ID
);
update member_info_0926 q, tmp set q.回答被举报平均数 = tmp.回答被举报平均数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 回答收到没有帮助平均数
create temporary table tmp as (
    select 用户ID, round(avg(回答收到的没有帮助数), 0) as 回答收到没有帮助平均数 from answer_info_0926 group by 用户ID
);
update member_info_0926 q, tmp set q.回答收到没有帮助平均数 = tmp.回答收到没有帮助平均数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 回答收到反对平均数
create temporary table tmp as (
    select 用户ID, round(avg(回答收到的反对数), 0) as 回答收到反对平均数 from answer_info_0926 group by 用户ID
);
update member_info_0926 q, tmp set q.回答收到反对平均数 = tmp.回答收到反对平均数 where q.用户ID = tmp.用户ID;
drop table tmp;
# 运行完成
```

