# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from finance.items import FinanceItem
from scrapy.loader.processors import MapCompose, Join


class LenovoSpider(scrapy.Spider):
    name = "Lenovo"
    start_urls = (
        'https://www.google.com/finance?q=HKG:0992&fstype=ii',
        'https://www.google.com/finance?cid=674788',
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
        l.add_xpath("QuarterlyCDPScore", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[7]/td[2]//text()',
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
        l.add_xpath("AnnualCDPScore", '//*[@id="gf-viewc"]/div/div/div[3]/div[1]/div/div[4]/table/tr[7]/td[3]//text()',
                    MapCompose(unicode.strip, unicode.title))



        #Quarterly IncomeStatement Start

        l.add_xpath("QuarterlyLenovoIncomeStatementCurrency", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoIncomeStatementTimePeriod", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTurnover", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoInterestIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoInterestExpense", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetInterestIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetFeeIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetTradingIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoOtherOperatingIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTotalOperatingIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetInsuranceClaimsIncurred", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetOperatingIncomeBeforeLoanImpairmentChargesAndProvisions", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTotalImpairmentCharagesAndProvisions", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetOperatingIncome", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTotalOperatingExpenses", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoOperatingProfit", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNonOperatingExceptionalItems", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoAssociates", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoProfitBeforeTaxation", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTaxation", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoProfitLossAfterTaxation", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoIncomeMinorityInterests", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoPreferenceShareDividend", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetProfit", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTotalDividend", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoRetainedProfitLoss", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoGrossProfit", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDepreciaton", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoIncomeStatementInterestPaid", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoInterestCapitalized", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTurnoverGrowth", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetProfitGrowth", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTaxationRate", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoEPSHKD", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDilutedEPSHKD", '//div[@id="incinterimdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))





        #Quarterly BalanceSheet Start


        l.add_xpath("QuarterlyLenovoBalanceSheetCurrency", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoBalanceSheetTimePeriod", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoCashAndShortTermFunds", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoItemsInTheCourseOfCollectionFromOtherBanks", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoPlacingsWithBanksAndOtherFinancialInstitutions", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTradingBills", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoCertificatesOfDepositHeld", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoHKGovernmentCertificatesOfIndebtedness", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTradingAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNonTradingAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoFinancialAssetsDesignatedAtFairValue", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDerivatives", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoLoansAndAdvancesToBanks", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoLoansAndAdvancesToCustomers", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoAvailableForSaleFinancialAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoFinancialInvestment", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoHeldToMaturityInvestmets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoInterestsInAssociatesAndJointVentures", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoGoodwillAndIntangibleAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoFixedAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoInvestments", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoCurrentAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoOtherAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoOtherAssets2", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTotalAssets", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoHKCurrencyNotesInCirculation", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDepositsAndBalancesOfBanksAndOtherFinancialInstitiutions", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDepositsFromCustomers", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoItemsInTheCourseOfTransmissionToOtherBanks", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTradingLiabilities", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoFinancialLiabilitiesDesignatedAtFairValues", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDerivatives2", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDebtInstrumentsInIssue", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoSubordinatedLiabilities", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoOtherLiabilities", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTotaLiabilities", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoShareCapital", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoSharePremium", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[36]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoRetainedProftsOrAccumulatedLosses", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoOtherReserves", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoReserves", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoShareholdersFunds", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[40]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoBalanceMinorityInterests", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[41]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTotalCapitalResources", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[42]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTotalLiabCapResources", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[43]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoLongTermDebt", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[44]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoOtherLiabilities2", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[45]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoCurrentLiabilities", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[46]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoInventory", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[47]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoCashOnHand", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[48]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoShortTermDebt", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[49]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTotalDebt", '//div[@id="balinterimdiv"]//*[@id="fs-table"]/tbody/tr[50]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))




        #Quarterly CashFlow Start

        l.add_xpath("QuarterlyLenovoCashFlowCurrency", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[1]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoCashFlowTimePeriod", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/thead/tr/th[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoCashGeneratedFromOperations", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetCashFlowFromOperatingActivities", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoInterestRecieved", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoCashFlowInterestPaid", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDividendsRecieved", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDividendsPaid", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoTaxesPaidOrRefunded", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoAdditionsToFixedAssets", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoIncreaseInInvestments", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDisposalOfFixedAssets", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoDecreaseInInvestments", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetCashFlowWithRelatedParties", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNewLoans", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoLoansRepayment", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoFixedIncomeDebtInstruments", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoEquityFinancing", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetCashFlowWithRelatedParties2", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetEffectOfForeignExchangeRateChangesOthers", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoRepaymentOfFixedIncomeOrDebtInstruments", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetCashFlowFromFinancingActivities", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoNetCashFlowFromInvestingActivities", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoIncreaseDecreaseInCashAndCashEquivalents", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoCashAndCashEquivalentsAtBeginningOfYear", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("QuarterlyLenovoCashAndCashEquivalentsAtEndOfYear", '//div[@id="casinterimdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))



        # Annual IncomeStatement Start

        l.add_xpath("AnnualLenovoIncomeStatementCurrency",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/thead/tr/th[1]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoIncomeStatementTimePeriod",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/thead/tr/th[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTurnover", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoInterestIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoInterestExpense",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetInterestIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetFeeIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetTradingIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoOtherOperatingIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTotalOperatingIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetInsuranceClaimsIncurred",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetOperatingIncomeBeforeLoanImpairmentChargesAndProvisions",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTotalImpairmentCharagesAndProvisions",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetOperatingIncome",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTotalOperatingExpenses",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoOperatingProfit",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNonOperatingExceptionalItems",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoAssociates",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoProfitBeforeTaxation",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTaxation",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoProfitLossAfterTaxation",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoIncomeMinorityInterests",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoPreferenceShareDividend",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetProfit",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTotalDividend",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoRetainedProfitLoss",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoGrossProfit",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDepreciaton",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoIncomeStatementInterestPaid",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoInterestCapitalized",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTurnoverGrowth",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetProfitGrowth",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTaxationRate",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoEPSHKD", '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDilutedEPSHKD",
                    '//div[@id="incannualdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))


        # Annual BalanceSheet Start


        l.add_xpath("AnnualLenovoBalanceSheetCurrency",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/thead/tr/th[1]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoBalanceSheetTimePeriod",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/thead/tr/th[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoCashAndShortTermFunds",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoItemsInTheCourseOfCollectionFromOtherBanks",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoPlacingsWithBanksAndOtherFinancialInstitutions",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTradingBills",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoCertificatesOfDepositHeld",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoHKGovernmentCertificatesOfIndebtedness",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTradingAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNonTradingAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoFinancialAssetsDesignatedAtFairValue",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDerivatives",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoLoansAndAdvancesToBanks",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoLoansAndAdvancesToCustomers",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoAvailableForSaleFinancialAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoFinancialInvestment",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoHeldToMaturityInvestmets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoInterestsInAssociatesAndJointVentures",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoGoodwillAndIntangibleAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoFixedAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoInvestments",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoCurrentAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoOtherAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoOtherAssets2",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTotalAssets",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoHKCurrencyNotesInCirculation",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDepositsAndBalancesOfBanksAndOtherFinancialInstitiutions",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[25]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDepositsFromCustomers",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[26]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoItemsInTheCourseOfTransmissionToOtherBanks",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[27]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTradingLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[28]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoFinancialLiabilitiesDesignatedAtFairValues",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[29]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDerivatives2",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[30]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDebtInstrumentsInIssue",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[31]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoSubordinatedLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[32]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoOtherLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[33]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTotaLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[34]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoShareCapital",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[35]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoSharePremium",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[36]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoRetainedProftsOrAccumulatedLosses",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[37]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoOtherReserves",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[38]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoReserves",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[39]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoShareholdersFunds",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[40]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoBalanceMinorityInterests",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[41]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTotalCapitalResources",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[42]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTotalLiabCapResources",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[43]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoLongTermDebt",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[44]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoOtherLiabilities2",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[45]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoCurrentLiabilities",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[46]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoInventory",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[47]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoCashOnHand",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[48]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoShortTermDebt",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[49]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTotalDebt",
                    '//div[@id="balannualdiv"]//*[@id="fs-table"]/tbody/tr[50]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))


        # Annual CashFlow Start

        l.add_xpath("AnnualLenovoCashFlowCurrency",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/thead/tr/th[1]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoCashFlowTimePeriod",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/thead/tr/th[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoCashGeneratedFromOperations",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[1]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetCashFlowFromOperatingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[2]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoInterestRecieved",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[3]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoCashFlowInterestPaid",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[4]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDividendsRecieved",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[5]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDividendsPaid",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[6]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoTaxesPaidOrRefunded",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[7]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoAdditionsToFixedAssets",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[8]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoIncreaseInInvestments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[9]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDisposalOfFixedAssets",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[10]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoDecreaseInInvestments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[11]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetCashFlowWithRelatedParties",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[12]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNewLoans",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[13]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoLoansRepayment",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[14]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoFixedIncomeDebtInstruments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[15]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoEquityFinancing",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[16]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetCashFlowWithRelatedParties2",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[17]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetEffectOfForeignExchangeRateChangesOthers",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[18]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoRepaymentOfFixedIncomeOrDebtInstruments",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[19]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetCashFlowFromFinancingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[20]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoNetCashFlowFromInvestingActivities",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[21]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoIncreaseDecreaseInCashAndCashEquivalents",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[22]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoCashAndCashEquivalentsAtBeginningOfYear",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[23]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))
        l.add_xpath("AnnualLenovoCashAndCashEquivalentsAtEndOfYear",
                    '//div[@id="casannualdiv"]//*[@id="fs-table"]/tbody/tr[24]/td[2]//text()',
                    MapCompose(unicode.strip, unicode.title))





        return l.load_item()