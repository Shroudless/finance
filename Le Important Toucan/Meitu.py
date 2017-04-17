# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from finance.items import FinanceItem
from scrapy.loader.processors import MapCompose, Join


class MeituSpider(scrapy.Spider):
    name = "Meitu"
    start_urls = (
        'https://www.google.com/finance?q=HKG:1357&fstype=ii',
        'https://www.google.com/finance?cid=428130012467999',
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

        l.add_xpath("QuarterlyPeriod", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/thead/tr/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyNetProfitMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyOperatingMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyEBITDMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyReturnOnAssets", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyReturnOnEquity", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyEmployees", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCDPScore", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyCDPScore",
                    '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[7]/td[2]/a/text()',
                    MapCompose(unicode.strip, unicode.title))

        #AnnualKeyRatios

        l.add_xpath("AnnualPeriod", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/thead/tr/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualNetProfitMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[1]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualOperatingMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[2]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualEBITDMargin", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[3]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualReturnOnAssets", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[4]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualReturnOnEquity", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[5]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualEmployees", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[6]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCDPScore", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[7]/td[3]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualCDPScore", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[7]/td[3]/a/text()',
                    MapCompose(unicode.strip, unicode.title))



        # Annual IncomeStatement Start

        l.add_xpath("MeituIncomeStatementCurrency",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituIncomeStatementTimePeriod",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTurnover", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituInterestIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituInterestExpense",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetInterestIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetFeeIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetTradingIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituOtherOperatingIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTotalOperatingIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetInsuranceClaimsIncurred",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetOperatingIncomeBeforeLoanImpairmentChargesAndProvisions",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTotalImpairmentChargesAndProvisions",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetOperatingIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTotalOperatingExpenses",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituOperatingProfit",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNonOperatingExceptionalItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituAssociates",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituProfitBeforeTaxation",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTaxation",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituProfitLossAfterTaxation",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituIncomeMinorityInterests",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituPreferenceShareDividend",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetProfit",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTotalDividend",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituRetainedProfitLoss",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituGrossProfit",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDepreciation",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituIncomeStatementInterestPaid",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituInterestCapitalized",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTurnoverGrowth",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetProfitGrowth",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTaxationRate",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituEPSHKD", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDilutedEPSHKD",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))

        # Negative Fields

        l.add_xpath("MeituOperatingProfit",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNonOperatingExceptionalItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituAssociates",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituProfitBeforeTaxation",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTaxation",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituProfitLossAfterTaxation",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituIncomeMinorityInterests",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetProfit",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTotalDividend",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituRetainedProfitLoss",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituGrossProfit",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTurnoverGrowth",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituEPSHKD",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDilutedEPSHKD",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))

        # Annual BalanceSheet Start


        l.add_xpath("MeituBalanceSheetCurrency",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituBalanceSheetTimePeriod",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCashAndShortTermFunds",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituItemsInTheCourseOfCollectionFromOtherBanks",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituPlacingsWithBanksAndOtherFinancialInstitutions",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTradingBills",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCertificatesOfDepositHeld",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituHKGovernmentCertificatesOfIndebtedness",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTradingAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNonTradingAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituFinancialAssetsDesignatedAtFairValue",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDerivatives",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituLoansAndAdvancesToBanks",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituLoansAndAdvancesToCustomers",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituAvailableForSaleFinancialAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituFinancialInvestment",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituHeldToMaturityInvestmets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituInterestsInAssociatesAndJointVentures",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituGoodwillAndIntangibleAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituFixedAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituInvestments",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCurrentAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituOtherAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituOtherAssets2",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTotalAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituHKCurrencyNotesInCirculation",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDepositsAndBalancesOfBanksAndOtherFinancialInstitiutions",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDepositsFromCustomers",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituItemsInTheCourseOfTransmissionToOtherBanks",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTradingLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituFinancialLiabilitiesDesignatedAtFairValues",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDerivatives2",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDebtInstrumentsInIssue",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituSubordinatedLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituOtherLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTotaLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituShareCapital",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituSharePremium",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[36]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituRetainedProftsOrAccumulatedLosses",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituOtherReserves",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituReserves",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituShareholdersFunds",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[40]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituBalanceMinorityInterests",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[41]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTotalCapitalResources",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[42]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTotalLiabCapResources",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[43]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituLongTermDebt",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[44]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituOtherLiabilities2",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[45]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCurrentLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[46]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituInventory",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[47]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCashOnHand",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[48]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituShortTermDebt",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[49]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTotalDebt",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[50]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))

        #Negative Fields

        l.add_xpath("MeituReserves",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituShareholdersFunds",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[40]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))

        # Annual CashFlow Start

        l.add_xpath("MeituCashFlowCurrency",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/thead/tr/th[1]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCashFlowTimePeriod",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/thead/tr/th[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCashGeneratedFromOperations",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetCashFlowFromOperatingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituInterestRecieved",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCashFlowInterestPaid",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDividendsRecieved",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDividendsPaid",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTaxesPaidOrRefunded",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituAdditionsToFixedAssets",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituIncreaseInInvestments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDisposalOfFixedAssets",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDecreaseInInvestments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetCashFlowWithRelatedParties",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNewLoans",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituLoansRepayment",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituFixedIncomeDebtInstruments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituEquityFinancing",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetCashFlowWithRelatedParties2",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetEffectOfForeignExchangeRateChangesOthers",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituRepaymentOfFixedIncomeOrDebtInstruments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetCashFlowFromFinancingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetCashFlowFromInvestingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituIncreaseDecreaseInCashAndCashEquivalents",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCashAndCashEquivalentsAtBeginningOfYear",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCashAndCashEquivalentsAtEndOfYear",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/text()',
                    MapCompose(unicode.strip, unicode.title))

        # Negative Fields

        l.add_xpath("MeituCashGeneratedFromOperations",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetCashFlowFromOperatingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituInterestRecieved",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCashFlowInterestPaid",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDividendsRecieved",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDividendsPaid",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituTaxesPaidOrRefunded",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituAdditionsToFixedAssets",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituIncreaseInInvestments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDisposalOfFixedAssets",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituDecreaseInInvestments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetCashFlowWithRelatedParties",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNewLoans",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituLoansRepayment",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituFixedIncomeDebtInstruments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituEquityFinancing",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetCashFlowWithRelatedParties2",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetEffectOfForeignExchangeRateChangesOthers",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituRepaymentOfFixedIncomeOrDebtInstruments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetCashFlowFromFinancingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituNetCashFlowFromInvestingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituIncreaseDecreaseInCashAndCashEquivalents",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCashAndCashEquivalentsAtBeginningOfYear",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("MeituCashAndCashEquivalentsAtEndOfYear",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]/span/text()',
                    MapCompose(unicode.strip, unicode.title))



        return l.load_item()