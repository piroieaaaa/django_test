from django.db import models

from users.models import User

"""
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

"""     # サンプル項目1 文字列
    sample_1 = models.CharField(
        verbose_name='サンプル項目1 文字列',
        max_length=20,
        blank=True,
        null=True,
    )

    # サンプル項目2 メモ
    sample_2 = models.TextField(
        verbose_name='サンプル項目2 メモ',
        blank=True,
        null=True,
    )

    # サンプル項目3 整数
    sample_3 = models.IntegerField(
        verbose_name='サンプル項目3 整数',
        blank=True,
        null=True,
    )

    # サンプル項目4 浮動小数点
    sample_4 = models.FloatField(
        verbose_name='サンプル項目4 浮動小数点',
        blank=True,
        null=True,
    )

    # サンプル項目5 固定小数点
    sample_5 = models.DecimalField(
        verbose_name='サンプル項目5 固定小数点',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )

    # サンプル項目6 ブール値
    sample_6 = models.BooleanField(
        verbose_name='サンプル項目6 ブール値',
    )

    # サンプル項目7 日付
    sample_7 = models.DateField(
        verbose_name='サンプル項目7 日付',
        blank=True,
        null=True,
    )

    # サンプル項目8 日時
    sample_8 = models.DateTimeField(
        verbose_name='サンプル項目8 日時',
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（固定）
    sample_9_choice = (
        (1, '選択１'),
        (2, '選択２'),
        (3, '選択３'),
    )

    sample_9 = models.IntegerField(
        verbose_name='サンプル項目9_選択肢（固定）',
        choices=sample_9_choice,
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（マスタ連動）
    sample_10 = models.ForeignKey(
        User,
        verbose_name='サンプル項目10_選択肢（マスタ連動）',
        blank=True,
        null=True,
        related_name='sample_10',
        on_delete=models.SET_NULL,
    ) """

class Item(models.Model):

    # 優先度
    priority_choice = (
        (1, '買う'),
        (2, '保留'),
    )

    priority = models.IntegerField(
        verbose_name='優先度',
        choices=priority_choice,
        default=priority_choice[0][0],
        blank=False,
        null=False,
    )

    # カテゴリ
    category_choice = (
        (1, '家具家電'),
        (2, '調理器具'),
        (3, '消耗品'),
        (4, '食器'),
        (99, 'その他'),
    )

    category = models.IntegerField(
        verbose_name='カテゴリ',
        choices=category_choice,
        default=category_choice[0][0],
        blank=False,
        null=False,
    )

    # 名称
    name = models.CharField(
        verbose_name='名称',
        max_length=30,
        blank=True,
        null=True,
    )

    # 予定金額
    plan_money = models.IntegerField(
        verbose_name='予定額',
        blank=True,
        null=True,
    )

    # 購入金額
    buy_money = models.IntegerField(
        verbose_name='購入額',
        blank=True,
        null=True,
    )

    # メモ
    memo = models.TextField(
        verbose_name='メモ',
        blank=True,
        null=True,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
