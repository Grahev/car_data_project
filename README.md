# Used Cars Market Analysis

This project aims to analyze the used cars market by scraping data from online platforms and performing data analysis. In this project, we will collect data on used cars, clean it, and perform basic analysis to understand trends in the market.

## Table of Contents

- [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Installation](#installation)
- [Data Scraping](#data-scraping)
- [Data Cleaning](#data-cleaning)
- [Data Analysis](#data-analysis)
- [Conclusion](#conclusion)

## Introduction

To get started with this project, you need basic knowledge of Python and the following tools:

### Requirements

- Python 3
- BeautifulSoup4
- Pandas
- Requests
- Scrapy

These tools can be installed using pip, which is a package manager for Python.

### Installation

To install the required packages, run the following command in the command prompt:


### Data Scraping

We will scrape data on used cars from online platforms such as Craigslist, eBay Motors, and Autotrader using the requests and BeautifulSoup4 packages. The code for scraping data is located in the scrape_data.py file.

The collected data will be saved to a SQLite database named database.csv.
Database location = scripts\crawlers\usedcarsni\database.db

### Data Cleaning

After collecting the data, we will clean it to remove any inconsistencies. The code for cleaning the data is located in the clean_data.py file.

The cleaned data will be saved to a new CSV file named cleaned_cars.csv.

### Data Analysis

After cleaning the data, we can perform basic data analysis. The code for data analysis is located in the analyze_data.py file.

In this project, we will analyze the following:

Top 10 most popular car models
Average price of cars by brand and model
Distribution of cars by age
Distribution of cars by mileage
Distribution of cars by location

### Conclusion

This project demonstrates the process of scraping data from online platforms, cleaning it, and performing data analysis to gain insights into the used cars market. You can use this project as a starting point for more advanced analyses or for analyzing other markets.


# Analiza Rynku Samochod??w U??ywanych

Ten projekt ma na celu analiz?? rynku samochod??w u??ywanych poprzez zbieranie danych z platform internetowych i przeprowadzenie analizy danych. W tym projekcie b??dziemy zbiera?? dane o samochodach u??ywanych, czy??ci?? je i przeprowadza?? podstawow?? analiz??, aby zrozumie?? trendy na rynku.

## Spis tre??ci

- [Wprowadzenie](#wprowadzenie)
  - [Wymagania](#wymagania)
  - [Instalacja](#instalacja)
- [Pobieranie Danych](#pobieranie-danych)
- [Czyszczenie Danych](#czyszczenie-danych)
- [Analiza danych](#analiza-danych)
- [Podsumowanie](#podsumowanie)

## Wprowadzenie

Aby rozpocz???? prac?? z tym projektem, potrzebujesz podstawowej wiedzy z zakresu j??zyka Python oraz nast??puj??cych narz??dzi:

### Wymagania

- Python 3
- BeautifulSoup4
- Pandas
- Requests
- Scrapy

Narz??dzia te mo??na zainstalowa?? za pomoc?? narz??dzia pip, kt??re jest menad??erem pakiet??w dla j??zyka Python.

### Instalacja

Aby zainstalowa?? wymagane pakiety, uruchom nast??puj??ce polecenie w wierszu polece??:


### Czyszczenie Danych

Po pobraniu danych oczy??cimy je, aby usun???? wszelkie niezgodno??ci. Kod do czyszczenia danych znajduje si?? w pliku clean_data.py.

Oczyszczone dane zostan?? zapisane w nowym pliku CSV o nazwie cleaned_cars.csv.

### Analiza Danych

Po oczyszczeniu danych mo??emy przeprowadzi?? podstawow?? analiz?? danych. Kod do analizy danych znajduje si?? w pliku analyze_data.py.

W tym projekcie b??dziemy analizowa?? nast??puj??ce elementy:

Top 10 najpopularniejszych modeli samochod??w
??rednia cena samochod??w wed??ug marki i modelu
Rozk??ad samochod??w wed??ug wieku
Rozk??ad samochod??w wed??ug przebiegu
Rozk??ad samochod??w wed??ug lokalizacji

### Podsumowanie

Ten projekt demonstruje proces pobierania danych z platform internetowych, oczyszczania ich i przeprowadzania analizy danych, aby uzyska?? wgl??d w rynek samochod??w u??ywanych. 