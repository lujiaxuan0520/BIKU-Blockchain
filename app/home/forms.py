# _*_ coding: utf-8 _*_
__author__ = 'mtianyan'
__date__ = '2017/8/26 17:07'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Regexp, EqualTo, ValidationError, Length
from app.models import User,Tag


class RegistForm(FlaskForm):
    name = StringField(
        label="昵称",
        validators=[
            DataRequired("昵称不能为空！")
        ],
        description="昵称",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入昵称！",
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("邮箱不能为空！"),
            Email("邮箱格式不正确！")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入邮箱！",
        }
    )
    phone = StringField(
        label="手机",
        validators=[
            DataRequired("手机号不能为空！"),
            Regexp("1[3458]\\d{9}", message="手机格式不正确！"),
            Length(min=11, max=11, message="手机长度不正确！")
        ],
        description="手机",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入手机！",
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空！")
        ],
        description="密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
        }
    )
    repwd = PasswordField(
        label="确认密码",
        validators=[
            DataRequired("请输入确认密码！"),
            EqualTo('pwd', message="两次密码不一致！")
        ],
        description="确认密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入确认密码！",
        }
    )
    submit = SubmitField(
        '注册',
        render_kw={
            "class": "btn btn-lg btn-success btn-block",
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("昵称已经存在！")

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("邮箱已经存在！")

    def validate_phone(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError("手机号码已经存在！")


class LoginForm(FlaskForm):
    name = StringField(
        label="账号",
        validators=[
            DataRequired("账号不能为空！")
        ],
        description="账号",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入账号！",
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空！")
        ],
        description="密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block",
        }
    )


class UserdetailForm(FlaskForm):
    name = StringField(
        label="账号",
        validators=[
            DataRequired("账号不能为空！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("邮箱不能为空！"),
            Email("邮箱格式不正确！")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！",
        }
    )
    phone = StringField(
        label="手机",
        validators=[
            DataRequired("手机号不能为空！"),
            Regexp("1[3458]\\d{9}", message="手机格式不正确！"),
            Length(min=11, max=11, message="手机长度不正确！")
        ],
        description="手机",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机！",
        }
    )
    face = FileField(
        label="头像",
        validators=[
            DataRequired("请上传头像！")
        ],
        description="头像",
    )
    info = TextAreaField(
        label="简介",
        validators=[
            DataRequired("简介不能为空！")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    submit = SubmitField(
        '保存修改',
        render_kw={
            "class": "btn btn-success",
        }
    )


class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        label="旧密码",
        validators=[
            DataRequired("旧密码不能为空！")
        ],
        description="旧密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码！",
        }
    )
    new_pwd = PasswordField(
        label="新密码",
        validators=[
            DataRequired("新密码不能为空！"),
        ],
        description="新密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码！",
        }
    )
    submit = SubmitField(
        '修改密码',
        render_kw={
            "class": "btn btn-success",
        }
    )


class CommentForm(FlaskForm):
    content = TextAreaField(
        label="内容",
        validators=[
            DataRequired("请输入内容！"),
        ],
        description="内容",
        render_kw={
            "id": "input_content"
        }
    )
    submit = SubmitField(
        '提交评论',
        render_kw={
            "class": "btn btn-success",
            "id": "btn-sub"
        }
    )


class MovieForm(FlaskForm):
    title = StringField(
        label="片名",
        validators=[
            DataRequired("片名不能为空！")
        ],
        description="片名",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "请输入片名！"
        }
    )
    url = FileField(
        label="文件",
        validators=[
            DataRequired("请上传文件！")
        ],
        description="文件",
    )
    info = TextAreaField(
        label="简介",
        validators=[
            DataRequired("简介不能为空！")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    logo = FileField(
        label="封面",
        validators=[
            DataRequired("请上传封面！")
        ],
        description="封面",
    )
    star = SelectField(
        label="星级",
        validators=[
            DataRequired("请选择星级！")
        ],
        # star的数据类型
        coerce=int,
        choices=[(1, "1星"), (2, "2星"), (3, "3星"), (4, "4星"), (5, "5星")],
        description="星级",
        render_kw={
            "class": "form-control",
        }
    )
    # 标签要在数据库中查询已存在的标签
    tag_id = SelectField(
        label="标签",
        validators=[
            DataRequired("请选择标签！")
        ],
        coerce=int,
        # 通过列表生成器生成列表
        choices=[(v.id, v.name) for v in Tag.query.all()],
        description="标签",
        render_kw={
            "class": "form-control",
        }
    )
    area = StringField(
        label="地区",
        #validators=[
        #    DataRequired("请输入地区！")
        #],
        description="地区",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入地区！"
        }
    )
    length = StringField(
        label="片长",
        #validators=[
        #    DataRequired("片长不能为空！")
        #],
        description="片长",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入片长！"
        }
    )
    release_time = StringField(
        label="上映时间",
        #validators=[
        #    DataRequired("上映时间不能为空！")
        #],
        description="上映时间",
        render_kw={
            "class": "form-control",
            "placeholder": "请选择上映时间！",
            "id": "input_release_time"
        }
    )
    submit = SubmitField(
        '添加',
        render_kw={
            "class": "btn btn-primary",
        }
    )