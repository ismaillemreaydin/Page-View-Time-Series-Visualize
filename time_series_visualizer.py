# time_series_visualizer.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini içe aktaralım
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Veriyi inceleyelim
print(df.head())
print(df.info())

# Gerekli görselleştirme fonksiyonlarını oluşturalım
def draw_line_plot():
    # Çizgi grafiği çizme işlemi burada gerçekleştirilecek
    pass

def draw_bar_plot():
    # Çubuk grafiği çizme işlemi burada gerçekleştirilecek
    pass

def draw_box_plot():
    # Kutu grafiğini çizme işlemi burada gerçekleştirilecek
    pass
#Şimdi, veriyi inceledikten sonra görselleştirme fonksiyonlarını oluşturalım. İlk olarak çizgi grafiğini çizme fonksiyonunu ekleyelim.


def draw_line_plot():
    # Veriyi temizleyelim (%2.5'lik dilimlerdeki verileri kaldırarak)
    df_cleaned = df[(df["value"] >= df["value"].quantile(0.025)) &
                    (df["value"] <= df["value"].quantile(0.975))]

    # Çizgi grafiğini çizelim
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df_cleaned.index, df_cleaned["value"], color='red')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    # X eksenindeki tarih etiketlerini daha okunaklı hale getirelim
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.xaxis.set_major_formatter(plt.DateFormatter("%Y-%m"))

    # Görüntüyü kaydedelim ve ekrana gösterelim
    plt.savefig("line_plot.png")
    plt.show()

    # Görüntüyü geri döndürelim
    return fig
#Şimdi, çubuk grafiğini çizme fonksiyonunu ekleyelim.


def draw_bar_plot():
    # Veriyi yıllara göre gruplayıp ortalama günlük sayfa görüntülemelerini hesaplayalım
    df_bar = df.groupby([df.index.year, df.index.month]).mean()
    df_bar = df_bar.unstack()

    # Çubuk grafiğini çizelim
    fig = df_bar.plot(kind='bar', figsize=(14, 7)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.title("Months")

    # X eksenindeki yıl etiketlerini daha okunaklı hale getirelim
    plt.xticks(rotation=45)
    plt.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    
    # Görüntüyü kaydedelim ve ekrana gösterelim
    plt.savefig("bar_plot.png")
    plt.show()

    # Görüntüyü geri döndürelim
    return fig
#Son olarak, kutu grafiğini çizme fonksiyonunu ekleyelim.


def draw_box_plot():
    # Veriyi yıllara ve aylara göre gruplayalım
    df_box_year = df.copy()
    df_box_year.reset_index(inplace=True)
    df_box_year['year'] = [d.year for d in df_box_year.date]
    df_box_year['month'] = [d.strftime('%b') for d in df_box_year.date]

    # Yıllara göre kutu grafiği çizelim
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))
    sns.boxplot(x='year', y='value', data=df_box_year, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Aylara göre kutu grafiği çizelim
    sns.boxplot(x='month', y='value', data=df_box_year, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Görüntüyü kaydedelim ve ekrana gösterelim
    plt.savefig("box_plot.png")
    plt.show()

    # Görüntüyü geri döndürelim
    return fig