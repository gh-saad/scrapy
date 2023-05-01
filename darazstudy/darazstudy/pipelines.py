# -*- coding: utf-8 -*-

from darazstudy.common import *

class DarazstudyExcelPipeline:
    rowNumb     = 0
    workbook    = xlsxwriter.Workbook('DarazstudyExcel.xlsx')
    worksheet   = workbook.add_worksheet("Final Data")
    worksheet.set_zoom(80)
    def __init__(self):
        self.rowNumb += 1
        self.worksheet.write( "A%s" % self.rowNumb, "p_href" )
        self.worksheet.write( "B%s" % self.rowNumb, "p_nid" )
        self.worksheet.write( "C%s" % self.rowNumb, "p_price" )
        self.worksheet.write( "D%s" % self.rowNumb, "p_type" )
        self.worksheet.write( "E%s" % self.rowNumb, "p_sku" )
        self.worksheet.write( "F%s" % self.rowNumb, "p_sellerid" )
        self.worksheet.write( "G%s" % self.rowNumb, "p_sellername" )
        self.worksheet.write( "H%s" % self.rowNumb, "p_categories" )
        self.worksheet.write( "I%s" % self.rowNumb, "p_rating" )
        self.worksheet.write( "J%s" % self.rowNumb, "p_reviews" )
        self.worksheet.write( "K%s" % self.rowNumb, "p_brandid" )
        self.worksheet.write( "L%s" % self.rowNumb, "p_brandname" )
        self.worksheet.write( "M%s" % self.rowNumb, "p_sold" )

    def process_item(self, item, spider):
        self.rowNumb += 1
        self.worksheet.write_string( "A%s" % self.rowNumb, item["p_href"] )
        self.worksheet.write_string( "B%s" % self.rowNumb, str(item["p_nid"]) )
        self.worksheet.write_string( "C%s" % self.rowNumb, item["p_price"] )
        self.worksheet.write_string( "D%s" % self.rowNumb, item["p_type"] )
        self.worksheet.write_string( "E%s" % self.rowNumb, str(item["p_sku"]) )
        self.worksheet.write_string( "F%s" % self.rowNumb, str(item["p_sellerid"]) )
        self.worksheet.write_string( "G%s" % self.rowNumb, item["p_sellername"] )
        self.worksheet.write_string( "H%s" % self.rowNumb, str(item["p_categories"]) )
        self.worksheet.write_string( "I%s" % self.rowNumb, str(item["p_rating"]) )
        self.worksheet.write_string( "J%s" % self.rowNumb, str(item["p_reviews"]) )
        self.worksheet.write_string( "K%s" % self.rowNumb, str(item["p_brandid"]) )
        self.worksheet.write_string( "L%s" % self.rowNumb, item["p_brandname"] )
        self.worksheet.write_string( "M%s" % self.rowNumb, str(item["p_sold"]) )
    
    def __del__(self):
        self.workbook.close()
