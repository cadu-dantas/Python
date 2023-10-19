import snowflake.connector
import holidays
from datetime import date
import access


#conecta no snowflake
ACCOUNT_SF=access.ACCOUNT_SF
USER_SF=access.USER_SF
PWD_SF=access.PWD_SF

try:
    sfConnection = sf.connect(
    user=USER_SF,
    password=PWD_SF,
    account=ACCOUNT_SF
    )
    sfq = sfConnection.cursor()
    sfq.execute("SELECT current_version()")
    sfResults = sfq.fetchall()
    #print('Snowflake Versao: ' + sfResults[0][0])
except:
    print("Verifique credenciais snowflake")
    exit(0)
# Conecte-se ao Snowflake
conn = snowflake.connector.connect(
    user=USER_SF,
    password=PWD_SF,
    account=ACCOUNT_SF,
    warehouse='WHDEV',
    database='TRADE',
    schema='TRANSIENT'
)

# Crie um cursor
cur = conn.cursor()

# Crie a tabela t_roliday no Snowflake se ela não existir
cur.execute('CREATE OR REPLACE TABLE TRADE.TRANSIENT.t_holiday (date DATE, holiday_name STRING)')

# Calcule e insira os feriados nacionais e regionais em São Paulo e Barueri de 2020 a 2100
for year in range(2020, 2101):
    br_holidays = holidays.Brazil(years=year)
    sp_holidays = holidays.Brazil(state='SP', years=year)
    barueri_holidays = holidays.Brazil(years=year, observed=False)  # Substitua pelo calendário de Barueri

    for date, name in br_holidays.items():
        cur.execute("INSERT INTO TRADE.TRANSIENT.t_holiday (date, holiday_name) VALUES (%s, %s)", (date, name))

    for date, name in sp_holidays.items():
        cur.execute("INSERT INTO TRADE.TRANSIENT.t_holiday (date, holiday_name) VALUES (%s, %s)", (date, name))

    for date, name in barueri_holidays.items():
        cur.execute("INSERT INTO TRADE.TRANSIENT.t_holiday (date, holiday_name) VALUES (%s, %s)", (date, name))

# Feche o cursor e a conexão com o Snowflake
cur.close()
conn.close()