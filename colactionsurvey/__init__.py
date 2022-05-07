from otree.api import *

author = 'Elena Smyslovskikh, HSE-Moscow'

doc = """
Questionnaire for research on collective action among Moscow students. 
"""


class C(BaseConstants):
    NAME_IN_URL = 'Опрос'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TREATMENTS = ['ingroup_success', 'ingroup_failure', 'outgroup_success', 'outgroup_success', 'control']


class Subsession(BaseSubsession):
    #xyz = models.IntegerField()
    pass


def creating_session(subsession: Subsession):
    import random
    for player in subsession.get_players():
        player.treatment = random.choice(['ingroup_success', 'ingroup_failure', 'outgroup_success', 'outgroup_failure', 'control'])
        print('set treatment to', player.treatment)


class Player(BasePlayer):
    treatment = models.IntegerField()
    final_treatment = models.CharField()
    age = models.IntegerField(
        label='<strong>Пожалуйста, укажите Ваш возраст (введите число)</strong>')
    gender = models.StringField(
        label='<strong>Пожалуйста, выберите Ваш пол</strong>',
        choices=['Мужской', 'Женский', 'предпочитаю не указывать']
    )
    university = models.StringField(
        label='<strong>Укажите Ваш вуз</strong>',
        choices=['МГУ', 'МФТИ', 'НИУ ВШЭ', 'МГИМО']
    )
    specialization = models.StringField(
        label='<strong>Укажите Ваше направление подготовки</strong>',
        choices=['МАТЕМАТИЧЕСКИЕ И ЕСТЕСТВЕННЫЕ НАУКИ',
                 'ИНЖЕНЕРНОЕ ДЕЛО, ТЕХНОЛОГИИ И ТЕХНИЧЕСКИЕ НАУКИ',
                 'ЗДРАВООХРАНЕНИЕ И МЕДИЦИНСКИЕ НАУКИ',
                 'СЕЛЬСКОЕ ХОЗЯЙСТВО И СЕЛЬСКОХОЗЯЙСТВЕННЫЕ НАУКИ',
                 'НАУКИ ОБ ОБЩЕСТВЕ',
                 'ОБРАЗОВАНИЕ И ПЕДАГОГИЧЕСКИЕ НАУКИ',
                 'ГУМАНИТАРНЫЕ НАУКИ',
                 'ИСКУССТВО И КУЛЬТУРА']
    )
    parent_educ = models.StringField(
        label='<strong>Укажите наивысший уровень образования (или ученую степень) Ваших родителей</strong>',
        choices=[
            'Средняя школа',
            'Среднее профессиональное образование',
            'Незаконченное высшее образование',
            'Высшее образование',
            'Два и более диплома / Ученая степень'
        ]
    )
    grievances_extent = models.IntegerField(
        label='<strong>Насколько Вы согласны с утверждением:</strong> "За время моего обучения в вузе возникали ситуации, '
              'представляющие проблему для студенческого сообщества"? <br />'
              '(1 - Абсолютно не согласен(-на), 5 - Полностью согласен(-на))',
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
    )
    blame_attr = models.StringField(
        label='<strong>Знаете ли Вы, какие из руководящих органов Вашего вуза занимаются решением проблем студентов?</strong>',
        choices=['Да, знаю, к кому обратиться лично', 'Да, что-то слышал(-а) об этих органах', 'Нет, не знаю'],
    )
    student_rights = models.StringField(
        label='<strong>Известно ли Вам о том, какие студенческие организации защищают интересы студентов?</strong>',
        choices=['Да, знаю, к кому обратиться лично', 'Да, что-то слышал(-а) об этих организациях', 'Нет, не знаю'],
    )
    identity_power = models.IntegerField(
        label='<strong>Насколько Вы согласны с утверждением:</strong> "Моя идентичность как студента моего вуза для меня первична"?<br />'
              '(1 - Абсолютно не согласен(-на), 5 - Полностью согласен(-на))',
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
    )
    activism = models.IntegerField(
        label='<strong>Участвовали ли Вы за последний год в каком-либо из следующих видов активности:</strong> <br />'
              '1) Публично выражали свою позицию по поводу значимой общественной проблемы <br />'
              '2) Участвовали (формально или неформально) в общественных организациях <br />'
              '3) Занимались волонтерством <br />'
              '(1 - Нет, не участвовал(-а), 5 - Да, участвовал(-а) неоднократно)',
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
    )
    trust = models.IntegerField(
        label='<strong>Насколько Вы согласны с утверждением:</strong> "Большинству людей можно доверять"? <br />'
              '(1 - Абсолютно не согласен(-на), 5 - Полностью согласен(-на))',
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal
    )
    participation = models.StringField(
        label='',
        choices=['Да, неоднократно', 'Да, однократно', 'Не обращался(-ась)'],
    )
    norms_participation = models.StringField(
        label='Представьте, что Ваш поток столкнулся с явной дискриминацией и/или нарушением прав небольшой группы студентов. <br />'
              'Вы не знакомы лично со студентами, которых это напрямую коснулось, однако ситуация стала известной и обсуждаемой среди учащихся. '
              'Известно также, что никакой реакции от руководства не последовало, хотя обращения были и прошло значительное количество времени. <br />'
              '<br>'
            'Считаете ли Вы, что студенты (в том числе Вы сами) должны вмешаться и коллективно потребовать от администрации рассмотреть возникшую ситуацию?',
        choices=['Да, должны вмешаться', 'Не должны вмешиваться', 'У студентов нет никаких обязательств']
    )
    norms_intensity = models.IntegerField(
        label='<strong>Насколько Вы согласны с утверждением:</strong> <br />"В ситуациях, которые потенциально могут повлиять на правопорядок в группе, каждый ее участник обязан активно выражать свою позицию"? <br />'
              '(1 - Абсолютно не согласен(-на), 9 - Полностью согласен(-на))',
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9],
        widget=widgets.RadioSelectHorizontal
    )


def generate_treatment_for_university(player: Player):
    import random
    ingroup_success = ''
    ingroup_failure = ''
    outgroup_success = ''
    outgroup_failure = ''
    if player.university == 'МГИМО':
        ingroup_success = 'Например, в 2020 году руководство МГИМО приняло решение не продлевать контракт с преподавательницей в связи с ее политической позицией, что вызвало массовое недовольство студентов, которые высоко ценили ее работу и профессионализм. Учащиеся подписали коллективное письмо на имя декана, после чего руководство пошло навстречу студентам и контракт с преподавательницей продлили. '
        outgroup_success = random.choice([
            'Например, в 2018 году ученый совет ВШЭ принял новое Положение об организации промежуточной аттестации и текущего контроля успеваемости студентов, в котором, помимо прочего, предлагалось введение "блокирующих" элементов оценивания, которые не позволяли бы получить положительную оценку по предмету. Такое положение привело к массовому недовольству студентов, активному протесту и коллективному обращению к ученому совету и администрайии. В результате этих действий, руководство пошло навстречу студентам и меры "блокирующих оценок" были пересмотрены и смягчены.',
            'Например, в 2014 году на одном из факультетов МГУ возникла ситуация массового недовольства студентов в связи с тем, что администрация факультета ввела обязательный медосмотр для студентов, хотя существенных оснований для этого не было. Студенты факультета собрали подписи и коллективно обратились в администрацию с требованием отменить обязательный медосмотр, в результате чего администрация пошла навстречу и медосмотр отменили.',
            'Например, в 2020 году администрацией МФТИ было принято решение ввести пропускной режим на территории студгородка и установить шлагбаум на въезде, что вызвало массовое недовольство студентов. Студенты вуза коллективно подписали петицию и заявление против установки шлагбаума, в результате чего администрация пошла навстречу и планы по введению пропускного режима отменили.'
        ])
        ingroup_failure = 'Например, в 2021 году руководство МГИМО приняло решение о недопуске к очной форме обучения студентов, которые не прошли вакцинацию от COVID-19, что вызвало массовое недовольство студентов. Учащиеся подписали коллективное письмо на имя ректора, однако положительного ответа от руководства не последовало. '
        outgroup_failure = random.choice([
            'Например, в 2020 году в связи с эпидемией COVID-19 администрация ВШЭ приняла решение об обязательном использовании системы прокторинга "Экзамус". Данная система на тот момент имела ряд существенных недостатков в работе, что вызвало массовое недовольство студентов. В связи с этим, студенты коллективно подписали открытое письмо за пересмотр решений по вопросу прокторинга, однако положительного решения администрации не последовало.',
            'Например, в связи с эпидемией COVID-19, руководство МГУ ужесточило правила прохода студентов и аспирантов в общежития и на факультеты, что вызвало массовое недовольство студентов. В 2021 году было направлено коллективное обращение с требованиями отменить ограничения на правила прохода в общежития и учебные корпуса, однако добиться отмены этих ограничений не удалось.',
            'Например, в 2021 году в студгородке МФТИ появилась возможность использовать здание котельной для внеучебной деятельности студентов, которую поддержало большое количество студентов, поскольку пространство для досуга на кампусе весьма ограничено. В связи с этим, было подано коллективное обращение и петиция с требованием не передавать здание под другие нужды, однако администрация вуза не пошла навстречу и добиться передачи здания под нужды студентов не удалось.'
        ])

    if player.university == 'НИУ ВШЭ':
        ingroup_success = 'Например, в 2018 году ученый совет ВШЭ принял новое Положение об организации промежуточной аттестации и текущего контроля успеваемости студентов, в котором, помимо прочего, предлагалось введение "блокирующих" элементов оценивания, которые не позволяли бы получить положительную оценку по предмету. Такое положение привело к массовому недовольству студентов, активному протесту и коллективному обращению к ученому совету и администрайии. В результате этих действий, руководство пошло навстречу студентам и меры "блокирующих оценок" были пересмотрены и смягчены.'
        outgroup_success = random.choice([
            'Например, в 2020 году руководство МГИМО приняло решение не продлевать контракт с преподавательницей в связи с ее политической позицией, что вызвало массовое недовольство студентов, которые высоко ценили ее работу и профессионализм. Учащиеся подписали коллективное письмо на имя декана, после чего руководство пошло навстречу студентам и контракт с преподавательницей продлили. ',
            'Например, в 2014 году на одном из факультетов МГУ возникла ситуация массового недовольства студентов в связи с тем, что администрация факультета ввела обязательный медосмотр для студентов, хотя существенных оснований для этого не было. Студенты факультета собрали подписи и коллективно обратились в администрацию с требованием отменить обязательный медосмотр, в результате чего администрация пошла навстречу и медосмотр отменили.',
            'Например, в 2020 году администрацией МФТИ было принято решение ввести пропускной режим на территории студгородка и установить шлагбаум на въезде, что вызвало массовое недовольство студентов. Студенты вуза коллективно подписали петицию и заявление против установки шлагбаума, в результате чего администрация пошла навстречу и планы по введению пропускного режима отменили.'
        ])
        ingroup_failure = 'Например, в 2020 году в связи с эпидемией COVID-19 администрация ВШЭ приняла решение об обязательном использовании системы прокторинга "Экзамус". Данная система на тот момент имела ряд существенных недостатков в работе, что вызвало массовое недовольство студентов. В связи с этим, студенты коллективно подписали открытое письмо за пересмотр решений по вопросу прокторинга, однако положительного решения администрации не последовало.'
        outgroup_failure = random.choice([
            'Например, в 2021 году руководство МГИМО приняло решение о недопуске к очной форме обучения студентов, которые не прошли вакцинацию от COVID-19, что вызвало массовое недовольство студентов. Учащиеся подписали коллективное письмо на имя ректора, однако положительного ответа от руководства не последовало. ',
            'Например, в связи с эпидемией COVID-19, руководство МГУ ужесточило правила прохода студентов и аспирантов в общежития и на факультеты, что вызвало массовое недовольство студентов. В 2021 году было направлено коллективное обращение с требованиями отменить ограничения на правила прохода в общежития и учебные корпуса, однако добиться отмены этих ограничений не удалось.',
            'Например, в 2021 году в студгородке МФТИ появилась возможность использовать здание котельной для внеучебной деятельности студентов, которую поддержало большое количество студентов, поскольку пространство для досуга на кампусе весьма ограничено. В связи с этим, было подано коллективное обращение и петиция с требованием не передавать здание под другие нужды, однако администрация вуза не пошла навстречу и добиться передачи здания под нужды студентов не удалось.'
        ])

    if player.university == 'МГУ':
        ingroup_success = 'Например, в 2014 году на одном из факультетов МГУ возникла ситуация массового недовольства студентов в связи с тем, что администрация факультета ввела обязательный медосмотр для студентов, хотя существенных оснований для этого не было. Студенты факультета собрали подписи и коллективно обратились в администрацию с требованием отменить обязательный медосмотр, в результате чего администрация пошла навстречу и медосмотр отменили.'
        outgroup_success = random.choice([
            'Например, в 2020 году руководство МГИМО приняло решение не продлевать контракт с преподавательницей в связи с ее политической позицией, что вызвало массовое недовольство студентов, которые высоко ценили ее работу и профессионализм. Учащиеся подписали коллективное письмо на имя декана, после чего руководство пошло навстречу студентам и контракт с преподавательницей продлили. ',
            'Например, в 2018 году ученый совет ВШЭ принял новое Положение об организации промежуточной аттестации и текущего контроля успеваемости студентов, в котором, помимо прочего, предлагалось введение "блокирующих" элементов оценивания, которые не позволяли бы получить положительную оценку по предмету. Такое положение привело к массовому недовольству студентов, активному протесту и коллективному обращению к ученому совету и администрайии. В результате этих действий, руководство пошло навстречу студентам и меры "блокирующих оценок" были пересмотрены и смягчены.',
            'Например, в 2020 году администрацией МФТИ было принято решение ввести пропускной режим на территории студгородка и установить шлагбаум на въезде, что вызвало массовое недовольство студентов. Студенты вуза коллективно подписали петицию и заявление против установки шлагбаума, в результате чего администрация пошла навстречу и планы по введению пропускного режима отменили.'
        ])
        ingroup_failure = 'Например, в связи с эпидемией COVID-19, руководство МГУ ужесточило правила прохода студентов и аспирантов в общежития и на факультеты, что вызвало массовое недовольство студентов. В 2021 году было направлено коллективное обращение с требованиями отменить ограничения на правила прохода в общежития и учебные корпуса, однако добиться отмены этих ограничений не удалось.'
        outgroup_failure = random.choice([
            'Например, в 2021 году руководство МГИМО приняло решение о недопуске к очной форме обучения студентов, которые не прошли вакцинацию от COVID-19, что вызвало массовое недовольство студентов. Учащиеся подписали коллективное письмо на имя ректора, однако положительного ответа от руководства не последовало. ',
            'Например, в 2020 году в связи с эпидемией COVID-19 администрация ВШЭ приняла решение об обязательном использовании системы прокторинга "Экзамус". Данная система на тот момент имела ряд существенных недостатков в работе, что вызвало массовое недовольство студентов. В связи с этим, студенты коллективно подписали открытое письмо за пересмотр решений по вопросу прокторинга, однако положительного решения администрации не последовало.',
            'Например, в 2021 году в студгородке МФТИ появилась возможность использовать здание котельной для внеучебной деятельности студентов, которую поддержало большое количество студентов, поскольку пространство для досуга на кампусе весьма ограничено. В связи с этим, было подано коллективное обращение и петиция с требованием не передавать здание под другие нужды, однако администрация вуза не пошла навстречу и добиться передачи здания под нужды студентов не удалось.'
        ])

    if player.university == 'МФТИ':
        ingroup_success = 'Например, в 2020 году администрацией МФТИ было принято решение ввести пропускной режим на территории студгородка и установить шлагбаум на въезде, что вызвало массовое недовольство студентов. Студенты вуза коллективно подписали петицию и заявление против установки шлагбаума, в результате чего администрация пошла навстречу и планы по введению пропускного режима отменили.'
        outgroup_success = random.choice([
            'Например, в 2020 году руководство МГИМО приняло решение не продлевать контракт с преподавательницей в связи с ее политической позицией, что вызвало массовое недовольство студентов, которые высоко ценили ее работу и профессионализм. Учащиеся подписали коллективное письмо на имя декана, после чего руководство пошло навстречу студентам и контракт с преподавательницей продлили. ',
            'Например, в 2018 году ученый совет ВШЭ принял новое Положение об организации промежуточной аттестации и текущего контроля успеваемости студентов, в котором, помимо прочего, предлагалось введение "блокирующих" элементов оценивания, которые не позволяли бы получить положительную оценку по предмету. Такое положение привело к массовому недовольству студентов, активному протесту и коллективному обращению к ученому совету и администрайии. В результате этих действий, руководство пошло навстречу студентам и меры "блокирующих оценок" были пересмотрены и смягчены.',
            'Например, в 2014 году на одном из факультетов МГУ возникла ситуация массового недовольства студентов в связи с тем, что администрация факультета ввела обязательный медосмотр для студентов, хотя существенных оснований для этого не было. Студенты факультета собрали подписи и коллективно обратились в администрацию с требованием отменить обязательный медосмотр, в результате чего администрация пошла навстречу и медосмотр отменили.'
        ])
        ingroup_failure = 'Например, в 2021 году в студгородке МФТИ появилась возможность использовать здание котельной для внеучебной деятельности студентов, которую поддержало большое количество студентов, поскольку пространство для досуга на кампусе весьма ограничено. В связи с этим, было подано коллективное обращение и петиция с требованием не передавать здание под другие нужды, однако администрация вуза не пошла навстречу и добиться передачи здания под нужды студентов не удалось.'
        outgroup_failure = random.choice([
            'Например, в 2021 году руководство МГИМО приняло решение о недопуске к очной форме обучения студентов, которые не прошли вакцинацию от COVID-19, что вызвало массовое недовольство студентов. Учащиеся подписали коллективное письмо на имя ректора, однако положительного ответа от руководства не последовало. ',
            'Например, в 2020 году в связи с эпидемией COVID-19 администрация ВШЭ приняла решение об обязательном использовании системы прокторинга "Экзамус". Данная система на тот момент имела ряд существенных недостатков в работе, что вызвало массовое недовольство студентов. В связи с этим, студенты коллективно подписали открытое письмо за пересмотр решений по вопросу прокторинга, однако положительного решения администрации не последовало.',
            'Например, в связи с эпидемией COVID-19, руководство МГУ ужесточило правила прохода студентов и аспирантов в общежития и на факультеты, что вызвало массовое недовольство студентов. В 2021 году было направлено коллективное обращение с требованиями отменить ограничения на правила прохода в общежития и учебные корпуса, однако добиться отмены этих ограничений не удалось.'
        ])
    treatments = [ingroup_success, ingroup_failure, outgroup_success, outgroup_failure]
    return treatments


class Group(BaseGroup):
    pass


# PAGES
class Intro(Page):
    pass


class ControlVars(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'university', 'specialization', 'parent_educ']


class IdentityQuestions(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        def get_treatment(player: Player):
            treatments = generate_treatment_for_university(player)
            if player.treatment == 'ingroup_success':
                final_treatment = treatments[0]
            elif player.treatment == 'ingroup_failure':
                final_treatment = treatments[1]
            elif player.treatment == 'outgroup_success':
                final_treatment = treatments[2]
            elif player.treatment == 'outgroup_failure':
                final_treatment = treatments[3]
            else:
                final_treatment = ''
            return final_treatment

        player.final_treatment = get_treatment(player)

    form_model = 'player'
    form_fields = ['activism', 'trust', 'identity_power', 'grievances_extent', 'blame_attr', 'student_rights']


class Treatments(Page):
    form_model = 'player'
    form_fields = ['participation']


class NormsQuestions(Page):
    form_model = 'player'
    form_fields = ['norms_participation', 'norms_intensity']


page_sequence = [Intro, ControlVars, IdentityQuestions, Treatments, NormsQuestions]

