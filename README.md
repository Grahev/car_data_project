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


# Analiza Rynku Samochodów Używanych

Ten projekt ma na celu analizę rynku samochodów używanych poprzez zbieranie danych z platform internetowych i przeprowadzenie analizy danych. W tym projekcie będziemy zbierać dane o samochodach używanych, czyścić je i przeprowadzać podstawową analizę, aby zrozumieć trendy na rynku.

## Spis treści

- [Wprowadzenie](#wprowadzenie)
  - [Wymagania](#wymagania)
  - [Instalacja](#instalacja)
- [Pobieranie Danych](#pobieranie-danych)
- [Czyszczenie Danych](#czyszczenie-danych)
- [Analiza danych](#analiza-danych)
- [Podsumowanie](#podsumowanie)

## Wprowadzenie

Aby rozpocząć pracę z tym projektem, potrzebujesz podstawowej wiedzy z zakresu języka Python oraz następujących narzędzi:

### Wymagania

- Python 3
- BeautifulSoup4
- Pandas
- Requests
- Scrapy

Narzędzia te można zainstalować za pomocą narzędzia pip, które jest menadżerem pakietów dla języka Python.

### Instalacja

Aby zainstalować wymagane pakiety, uruchom następujące polecenie w wierszu poleceń:


### Czyszczenie Danych

Po pobraniu danych oczyścimy je, aby usunąć wszelkie niezgodności. Kod do czyszczenia danych znajduje się w pliku clean_data.py.

Oczyszczone dane zostaną zapisane w nowym pliku CSV o nazwie cleaned_cars.csv.

### Analiza Danych

Po oczyszczeniu danych możemy przeprowadzić podstawową analizę danych. Kod do analizy danych znajduje się w pliku analyze_data.py.

W tym projekcie będziemy analizować następujące elementy:

Top 10 najpopularniejszych modeli samochodów
Średnia cena samochodów według marki i modelu
Rozkład samochodów według wieku
Rozkład samochodów według przebiegu
Rozkład samochodów według lokalizacji

### Podsumowanie

Ten projekt demonstruje proces pobierania danych z platform internetowych, oczyszczania ich i przeprowadzania analizy danych, aby uzyskać wgląd w rynek samochodów używanych. 