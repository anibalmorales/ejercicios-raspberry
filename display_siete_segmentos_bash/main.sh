#    Programado por Luis Cabrera Benito
#  ____          _____               _ _           _
# |  _ \        |  __ \             (_) |         | |
# | |_) |_   _  | |__) |_ _ _ __ _____| |__  _   _| |_ ___
# |  _ <| | | | |  ___/ _` | '__|_  / | '_ \| | | | __/ _ \
# | |_) | |_| | | |  | (_| | |   / /| | |_) | |_| | ||  __/
# |____/ \__, | |_|   \__,_|_|  /___|_|_.__/ \__, |\__\___|
#         __/ |                               __/ |
#        |___/                               |___/
#
#
#    Blog:       https://parzibyte.me/blog
#    Ayuda:      https://parzibyte.me/blog/contrataciones-ayuda/
#    Contacto:   https://parzibyte.me/blog/contacto/
G=12
F=14
A=15
B=18
C=23
D=17
E=27
for NUMERO in $A $B $C $D $E $F $G; do
    echo "Colocando modo out a $NUMERO ... OK :)"
    gpio -g mode $NUMERO out
    gpio -g write $NUMERO 0
done

# Un ejemplo para dibujar el número 6, que sería:
# 1011111

for NUMERO in $A $C $D $E $F $G; do
    gpio -g write $NUMERO 1
done

echo "Terminado"
