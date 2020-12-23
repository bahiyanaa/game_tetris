импортировать  pygame
из  копирования  импорт  deepcopy
из  случайного  выбора импорта  , randrange

Ш , В  =  10 , 20
ПЛИТКА  =  45
GAME_RES  =  Ш  *  ПЛИТКА , В  *  ПЛИТКА
RES  =  750 , 940
FPS  =  60

pygame . init ()
sc  =  pygame . дисплей . set_mode ( RES )
game_sc  =  pygame . Поверхность ( GAME_RES )
часы  =  pygame . время . Часы ()

сетка  = [ pygame . Rect ( x  *  TILE , y  *  TILE , TILE , TILE ) для  x  в  диапазоне ( W ) для  y  в  диапазоне ( H )]

цифры_pos  = [[( - 1 , 0 ), ( - 2 , 0 ), ( 0 , 0 ), ( 1 , 0 )],
               [( 0 , - 1 ), ( - 1 , - 1 ), ( - 1 , 0 ), ( 0 , 0 )],
               [( - 1 , 0 ), ( - 1 , 1 ), ( 0 , 0 ), ( 0 , - 1 )],
               [( 0 , 0 ), ( - 1 , 0 ), ( 0 , 1 ), ( - 1 , - 1 )],
               [( 0 , 0 ), ( 0 , - 1 ), ( 0 , 1 ), ( - 1 , - 1 )],
               [( 0 , 0 ), ( 0 , - 1 ), ( 0 , 1 ), ( 1 , - 1 )],
               [( 0 , 0 ), ( 0 , - 1 ), ( 0 , 1 ), ( - 1 , 0 )]]

цифры  = [[ pygame . Rect ( x  +  W  //  2 , y  +  1 , 1 , 1 ) для  x , y  на  fig_pos ] для  fig_pos  на  figure_pos ]
figure_rect  =  pygame . Rect ( 0 , 0 , TILE  -  2 , TILE  -  2 )
field  = [[ 0  для  i  в  диапазоне ( W )] для  j  в  диапазоне ( H )]

anim_count , anim_speed , anim_limit  =  0 , 60 , 2000

bg  =  pygame . изображение . загрузить ( 'img / bg.jpg' ). convert ()
game_bg  =  pygame . изображение . загрузить ( 'img / bg2.jpg' ). convert ()

main_font  =  pygame . шрифт . Шрифт ( 'font / font.ttf' , 65 )
font  =  pygame . шрифт . Шрифт ( 'font / font.ttf' , 45 )

title_tetris  =  main_font . render ( 'TETRIS' , True , pygame . Color ( 'darkorange' ))
title_score  =  шрифт . render ( 'score:' , True , pygame . Color ( 'зеленый' ))
title_record  =  шрифт . render ( 'record:' , True , pygame . Color ( 'purple' ))

get_color  =  лямбда : ( randrange ( 30 , 256 ), randrange ( 30 , 256 ), randrange ( 30 , 256 ))

рисунок , next_figure  =  deepcopy ( выбор ( цифры )), deepcopy ( выбор ( цифры ))
цвет , next_color  =  get_color (), get_color ()

оценка , линии  =  0 , 0
оценка  = { 0 : 0 , 1 : 100 , 2 : 300 , 3 : 700 , 4 : 1500 }


def  check_borders ():
    если  цифра [ i ]. x  <  0  или  цифра [ i ]. x  >  W  -  1 :
        return  False
    elif  рисунок [ i ]. y  >  H  -  1  или  поле [ рисунок [ i ]. y ] [ рисунок [ i ]. x ]:
        return  False
    вернуть  True


def  get_record ():
    попробуйте :
        с  open ( 'record' ) как  f :
            возврат  f . readline ()
    кроме  FileNotFoundError :
        с  open ( 'record' , 'w' ) как  f :
            f . написать ( '0' )


def  set_record ( запись , оценка ):
    rec  =  max ( int ( запись ), оценка )
    с  open ( 'record' , 'w' ) как  f :
        f . написать ( str ( rec ))


в то время как  True :
    запись  =  get_record ()
    dx , rotate  =  0 , ложь
    sc . блит ( bg , ( 0 , 0 ))
    sc . Blit ( game_sc , ( 20 , 20 ))
    game_sc . Blit ( game_bg , ( 0 , 0 ))
    # задержка для целых строк
    для  i  в  диапазоне ( строки ):
        pygame . время . ждать ( 200 )
    # контроль
    для  события  в  pygame . событие . получить ():
        если  событие . введите  ==  pygame . ВЫЙТИ :
            выход ()
        если  событие . введите  ==  pygame . КЛЮЧ :
            если  событие . ключ  ==  pygame . K_LEFT :
                dx  =  - 1
            elif  событие . ключ  ==  pygame . K_RIGHT :
                dx  =  1
            elif  событие . ключ  ==  pygame . K_DOWN :
                anim_limit  =  100
            elif  событие . ключ  ==  pygame . K_UP :
                rotate  =  True
    # переместить x
    figure_old  =  deepcopy ( рисунок )
    для  i  в  диапазоне ( 4 ):
        рисунок [ i ]. х  + =  dx
        если  не  check_borders ():
            figure  =  deepcopy ( figure_old )
            сломать
    # двигаться y
    anim_count  + =  anim_speed
    если  anim_count  >  anim_limit :
        anim_count  =  0
        figure_old  =  deepcopy ( рисунок )
        для  i  в  диапазоне ( 4 ):
            рисунок [ i ]. у  + =  1
            если  не  check_borders ():
                для  i  в  диапазоне ( 4
                    поле [ figure_old [ i ]. y ] [ figure_old [ i ]. x ] =  цвет
                рисунок , цвет  =  следующая_фигура , следующий_цвет
                next_figure , next_color  =  deepcopy ( выбор ( цифры )), get_color ()
                anim_limit  =  2000
                сломать
    # повернуть
    центр  =  фигура [ 0 ]
    figure_old  =  deepcopy ( рисунок )
    если  повернуть :
        для  i  в  диапазоне ( 4 ):
            x  =  цифра [ i ]. у  -  центр . y
            y  =  цифра [ i ]. х  -  центр . Икс
            рисунок [ i ]. x  =  центр . х  -  х
            рисунок [ i ]. y  =  центр . у  +  у
            если  не  check_borders ():
                figure  =  deepcopy ( figure_old )
                сломать
    # контрольные строки
    line , lines  =  H  -  1 , 0
    для  строки  в  диапазоне ( H  -  1 , - 1 , - 1 ):
        count  =  0
        для  i  в  диапазоне ( Вт ):
            если  поле [ строка ] [ i ]:
                count  + =  1
            поле [ строка ] [ i ] =  поле [ строка ] [ i ]
        если  count  <  W :
            линия  - =  1
        еще :
            anim_speed  + =  3
            линии  + =  1
    # вычислить оценку
    оценка  + =  баллы [ строки ]
    # рисовать сетку
    [ pygame . рисовать . rect ( game_sc , ( 40 , 40 , 40 ), i_rect , 1 ) для  i_rect  в  сетке ]
    # нарисовать фигуру
    для  i  в  диапазоне ( 4 ):
        figure_rect . x  =  цифра [ i ]. x  *  ПЛИТКА
        figure_rect . y  =  цифра [ i ]. y  *  ПЛИТКА
        pygame . рисовать . rect ( game_sc , цвет , рисунок_rect )
    # рисовать поле
    для  y , raw  в  enumerate ( поле ):
        для  x , столбец  в  перечислении ( необработанный ):
            если  col :
                figure_rect . х , фигура_рект . y  =  x  *  ПЛИТКА , y  *  ПЛИТКА
                pygame . рисовать . rect ( game_sc , col , figure_rect )
    # нарисовать следующую фигуру
    для  i  в  диапазоне ( 4 ):
        figure_rect . x  =  следующая_фигура [ i ]. x  *  ПЛИТКА  +  380
        figure_rect . y  =  следующая_фигура [ i ]. y  *  TILE  +  185
        pygame . рисовать . rect ( sc , next_color , figure_rect )
    # рисовать заголовки
    sc . Blit ( title_tetris , ( 485 , - 10 ))
    sc . Blit ( title_score , ( 535 , 780 ))
    sc . blit ( font . render ( str ( score ), True , pygame . Color ( 'white' )), ( 550 , 840 ))
    sc . Blit ( title_record , ( 525 , 650 ))
    sc . blit ( font . render ( record , True , pygame . Color ( 'gold' )), ( 550 , 710 ))
    # игра завершена
    для  i  в  диапазоне ( Вт ):
        если  поле [ 0 ] [ i ]:
            set_record ( запись , оценка )
            field  = [[ 0  для  i  в  диапазоне ( W )] для  i  в  диапазоне ( H )]
            anim_count , anim_speed , anim_limit  =  0 , 60 , 2000
            оценка  =  0
            для  i_rect  в  сетке :
                pygame . рисовать . rect ( game_sc , get_color (), i_rect )
                sc . Blit ( game_sc , ( 20 , 20 ))
                pygame . дисплей . перевернуть ()
                часы . галочка ( 200 )

    pygame . дисплей . перевернуть ()
    часы . галочка ( FPS )
