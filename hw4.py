# использование %
print('В команде Мастера кода участников: %s' % 5)
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!" % {'team1_num':5, 'team2_num':6})

# использование format
print('Команда Волшебники данных решила задач: {score_2}!'.format(score_2 = 42))
print('Волшебники данных решили задачи за {team1_time}с!'.format(team1_time = 18015.2))

# использование f-строк
score_1 = 40
score_2 = 42
challenge_result = 'Мастера кода'
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: победа команды {challenge_result}!')

tasks_total = 10
time_avg = 60
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунд на задачу!')
