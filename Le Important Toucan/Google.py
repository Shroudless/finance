# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from finance.items import FinanceItem
from scrapy.loader.processors import MapCompose, Join


class GoogleSpider(scrapy.Spider):
    name = "Google"
    start_urls = (
        'https://www.google.com/finance?q=NASDAQ:GOOGL&fstype=ii',
        'https://www.google.com/finance?cid=694653',
    )

    def parse(self, response):
        l = ItemLoader(item=FinanceItem(), response=response)
        l.add_xpath("CompanyName", '//*[@id="companyheader"]/div[1]/h3/text()',
                    MapCompose(unicode.strip, unicode.title))  # needs return value to output
        l.add_xpath("StockExchangeAndCode", '//*[@id="companyheader"]/div[1]/text()[1]',
                    MapCompose(unicode.strip, lambda i: i.split(',')[1].split(')')[0]))
        l.add_xpath("Currency", '//*[@id="ref_6826782_elt"]/div/div/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("Date", '//*[@id="ref_6826782_elt"]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("StockPrice", '//*[@id="ref_6826782_l"]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MarketCap", '//*[@id="market-data-div"]/div[2]/div[1]/table[1]/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("PE", '//*[@id="market-data-div"]/div[2]/div[1]/table[1]/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("EPS", '//*[@id="market-data-div"]/div[2]/div[1]/table[2]/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("Shares", '//*[@id="market-data-div"]/div[2]/div[1]/table[2]/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("InstOwn", '//*[@id="market-data-div"]/div[2]/div[1]/table[2]/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))

        #QuarterlyKeyRatios

        l.add_xpath("QuarterlyPeriod", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/thead/tr/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetProfitMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOperatingMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyEBITDMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyReturnOnAssets", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyReturnOnEquity", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyEmployees", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCDPScore", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))

        #AnnualKeyRatios

        l.add_xpath("AnnualPeriod", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/thead/tr/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetProfitMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[1]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOperatingMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[2]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualEBITDMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[3]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualReturnOnAssets", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[4]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualReturnOnEquity", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[5]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualEmployees", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[6]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCDPScore", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[6]/table/tr[7]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))

        #QuarterlyIncomeStatement


        l.add_xpath("QuarterlyIncomeSheetCurrency", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIncomeTimePeriod", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyRevenue", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherRevenueTotal", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalRevenue", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCostOfRevenueTotal", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyGrossProfit", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlySellingGeneralAdminExpensesTotal",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyResearchAndDevelopment", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDepreciationAmortization",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyInterestExpenseIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyUnusualExpenseIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherOperatingExpenses", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalOperatingExpenses", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOperatingIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyInterestIncomeExpense", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyGainLossOnSaleOfAssets", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherNet", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIncomeBeforeTax", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIncomeAfterTax", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyMinorityInterest", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyEquityInAffiliates", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetIncomeBeforeExtraItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyAccountingChange", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDiscontinuedOperations", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyExtraordinaryItem", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyPreferredDividends", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIncomeAvailabletoCommonExclExtraItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIncomeAvailabletoCommonInclExtraItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyBasicWeightedAverageShares",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyBasicEPSExcludingExtraordinaryItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyBasicEPSIncludingExtraordinaryItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDilutionAdjustment", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDilutedWeightedAverageShares",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDilutedEPSExcludingExtraordinaryItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDilutedEPSIncludingExtraordinaryItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDividendsperShareCommonStockPrimaryIssue",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[36]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyGrossDividendsCommonStock",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetIncomeAfterStockBasedCompExpense",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyBasicEPSAfterStockBasedCompExpense",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDilutedEPSAfterStockBasedCompExpense",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[40]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDepreciationSupplemental",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[41]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalSpecialItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[42]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNormalizedIncomeBeforeTaxes",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[43]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyEffectOfSpecialItemsOnIncomeTaxes",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[44]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIncomeTaxesExcludingImpactOfSpecialItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[45]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNormalizedIncomeAfterTaxes",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[46]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNormalizedIncomeAvailToCommon",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[47]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyBasicNormalizedEPS", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[48]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDilutedNormalizedEPS",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[49]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))

        #Negative Fields for IncomeStatement

        l.add_xpath("QuarterlyGrossProfit", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOperatingIncome",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyGainLossOnSaleOfAssets",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyGainLossOnSaleOfAssets",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherNet", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIncomeBeforeTax",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIncomeAfterTax",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetIncomeBeforeExtraItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetIncome",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDilutedEPSExcludingExtraordinaryItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDilutedEPSIncludingExtraordinaryItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDilutedNormalizedEPS",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[49]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIncomeAvailabletoCommonExclExtraItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIncomeAvailabletoCommonInclExtraItems",
                    '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))

        # AnnualIncomeStatement


        l.add_xpath("AnnualIncomeStatementCurrency", '//div[@id="incannualdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIncomeTimePeriod", '//div[@id="incannualdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualRevenue", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherRevenueTotal", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalRevenue", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCostOfRevenueTotal",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualGrossProfit", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualSellingGeneralAdminExpensesTotal",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualResearchAndDevelopment",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDepreciationAmortization",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualInterestExpenseIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualUnusualExpenseIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherOperatingExpenses",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalOperatingExpenses",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOperatingIncome", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualInterestIncomeExpense",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualGainLossOnSaleOfAssets",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherNet", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIncomeBeforeTax", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIncomeAfterTax", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualMinorityInterest", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualEquityInAffiliates",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetIncomeBeforeExtraItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualAccountingChange", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDiscontinuedOperations",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualExtraordinaryItem",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetIncome", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualPreferredDividends",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIncomeAvailabletoCommonExclExtraItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIncomeAvailabletoCommonInclExtraItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualBasicWeightedAverageShares",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualBasicEPSExcludingExtraordinaryItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualBasicEPSIncludingExtraordinaryItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDilutionAdjustment",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDilutedWeightedAverageShares",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDilutedEPSExcludingExtraordinaryItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDilutedEPSIncludingExtraordinaryItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDividendsperShareCommonStockPrimaryIssue",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[36]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualGrossDividendsCommonStock",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetIncomeAfterStockBasedCompExpense",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualBasicEPSAfterStockBasedCompExpense",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDilutedEPSAfterStockBasedCompExpense",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[40]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDepreciationSupplemental",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[41]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalSpecialItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[42]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNormalizedIncomeBeforeTaxes",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[43]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualEffectOfSpecialItemsOnIncomeTaxes",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[44]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIncomeTaxesExcludingImpactOfSpecialItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[45]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNormalizedIncomeAfterTaxes",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[46]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNormalizedIncomeAvailToCommon",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[47]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualBasicNormalizedEPS",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[48]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDilutedNormalizedEPS",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[49]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))

        # Negative Fields for IncomeStatement

        l.add_xpath("AnnualGrossProfit", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOperatingIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualGainLossOnSaleOfAssets",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualGainLossOnSaleOfAssets",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherNet", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIncomeBeforeTax",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIncomeAfterTax",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetIncomeBeforeExtraItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDilutedEPSExcludingExtraordinaryItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDilutedEPSIncludingExtraordinaryItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDilutedNormalizedEPS",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[49]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIncomeAvailabletoCommonExclExtraItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIncomeAvailabletoCommonInclExtraItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))




        #QuarterlyBalanceSheet


        l.add_xpath("QuarterlyBalanceTimePeriod", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyBalanceSheetCurrency", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashAndEquivalents", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyShortTermInvestments", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashAndShortTermInvestments",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyAccountsReceivableTradeNet",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyReceivablesOther", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalReceivablesNet", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalInventory", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyPrepaidExpenses", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherCurrentAssetsTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalCurrentAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyPropertyPlantEquipmentTotalGross",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyAccumulatedDepreciationTotal",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyGoodwillNet", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIntangiblesNet", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLongTermInvestments", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherLongTermAssetsTotal",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyAccountsPayable", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyAccruedExpenses", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNotesPayableShortTermDebt",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCurrentPortofLTDebtCapitalLeases",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherCurrentliabilitiesTotal",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalCurrentLiabilities",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLongTermDebt", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCapitalLeaseObligations",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalLongTermDebt", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalDebt", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDeferredIncomeTax", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyMinorityInterestBal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherLiabilitiesTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalLiabilities", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyRedeemablePreferredStockTotal",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyPreferredStockNonRedeemableNet",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCommonStockTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyAdditionalPaidInCapital",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyRetainedEarningsAccumulatedDeficit",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[36]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTreasuryStockCommon",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherEquityTotal", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalEquity", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalLiabilitiesShareholdersEquity",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[40]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlySharesOutsCommonStockPrimaryIssue",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[41]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalCommonSharesOutstanding",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[42]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))

        #Negative Fields for BalanceSheet

        l.add_xpath("QuarterlyAccumulatedDepreciationTotal",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTreasuryStockCommon",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherEquityTotal",
                    '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalEquity", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))

        # AnnualBalanceSheet


        l.add_xpath("AnnualBalanceTimePeriod", '//div[@id="balannualdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualBalanceSheetCurrency", '//div[@id="balannualdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashAndEquivalents",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualShortTermInvestments",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashAndShortTermInvestments",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualAccountsReceivableTradeNet",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualReceivablesOther", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalReceivablesNet",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalInventory", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualPrepaidExpenses", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherCurrentAssetsTotal",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalCurrentAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualPropertyPlantEquipmentTotalGross",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualAccumulatedDepreciationTotal",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualGoodwillNet", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIntangiblesNet", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLongTermInvestments",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherLongTermAssetsTotal",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalAssets", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualAccountsPayable", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualAccruedExpenses", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNotesPayableShortTermDebt",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCurrentPortofLTDebtCapitalLeases",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherCurrentliabilitiesTotal",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalCurrentLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLongTermDebt", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCapitalLeaseObligations",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalLongTermDebt",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalDebt", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDeferredIncomeTax",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualMinorityInterestBal",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherLiabilitiesTotal",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalLiabilities", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualRedeemablePreferredStockTotal",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualPreferredStockNonRedeemableNet",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCommonStockTotal", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualAdditionalPaidInCapital",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualRetainedEarningsAccumulatedDeficit",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[36]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTreasuryStockCommon",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherEquityTotal", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalEquity", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalLiabilitiesShareholdersEquity",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[40]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualSharesOutsCommonStockPrimaryIssue",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[41]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalCommonSharesOutstanding",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[42]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))

        # Negative Fields for BalanceSheet

        l.add_xpath("AnnualAccumulatedDepreciationTotal",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTreasuryStockCommon",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherEquityTotal",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalEquity", '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))


        #QuarterlyCashFlow

        l.add_xpath("QuarterlyCashFlowCurrency", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashTimePeriod", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetIncomeStartingLine",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDepreciationDepreciation",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyAmortization", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDeferredTaxes", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNonCashItems", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyChangesInWorkingCapital", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashFromOperatingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCapitalExpenditures",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherInvestingCashFlowItemsTotal",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashFromInvestingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyFinancingCashFlowItems",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalCashDividendsPaid", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIssuanceRetirementofStockNet",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIssuanceRetitementOfDebtNet",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashFromFinancingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyForeignExchangeEffects", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetChangeInCash", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashInterestPaidSupplemental",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashTaxesPaidSupplemental",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))

        #Negative Fields

        l.add_xpath("QuarterlyCashFlowCurrency", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashTimePeriod", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetIncomeStartingLine",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDepreciationDepreciation",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyAmortization", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyDeferredTaxes",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNonCashItems", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyChangesInWorkingCapital",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashFromOperatingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCapitalExpenditures",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOtherInvestingCashFlowItemsTotal",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashFromInvestingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyFinancingCashFlowItems",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyTotalCashDividendsPaid",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIssuanceRetirementofStockNet",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyIssuanceRetitementOfDebtNet",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashFromFinancingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyForeignExchangeEffects",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetChangeInCash",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashInterestPaidSupplemental",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCashTaxesPaidSupplemental",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))


        #AnnualCashFlow


        l.add_xpath("AnnualCashFlowCurrency", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashTimePeriod", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetIncomeStartingLine",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDepreciationDepreciation",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualAmortization", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDeferredTaxes", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNonCashItems", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualChangesInWorkingCapital",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashFromOperatingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCapitalExpenditures",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherInvestingCashFlowItemsTotal",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashFromInvestingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualFinancingCashFlowItems",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalCashDividendsPaid",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIssuanceRetirementofStockNet",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIssuanceRetitementOfDebtNet",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashFromFinancingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualForeignExchangeEffects",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetChangeInCash",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashInterestPaidSupplemental",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashTaxesPaidSupplemental",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))


        # Negative Fields


        l.add_xpath("AnnualCashFlowCurrency",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashTimePeriod",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetIncomeStartingLine",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDepreciationDepreciation",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualAmortization",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualDeferredTaxes",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNonCashItems",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualChangesInWorkingCapital",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashFromOperatingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCapitalExpenditures",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOtherInvestingCashFlowItemsTotal",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashFromInvestingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualFinancingCashFlowItems",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualTotalCashDividendsPaid",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIssuanceRetirementofStockNet",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualIssuanceRetitementOfDebtNet",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashFromFinancingActivities",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualForeignExchangeEffects",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetChangeInCash",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashInterestPaidSupplemental",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCashTaxesPaidSupplemental",
                    '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))








        return l.load_item()