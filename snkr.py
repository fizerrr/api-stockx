class Snkr:
      name = None
      shoe = None
      imageUrl = None
      smallImageUrl = None
      thumbUrl = None
      retailPrice = None
      year = None
      lowestAsk = None
      lowestAskSize = None
      highestBidSize = None
      deadstockRangeLow = None
      deadstockRangeHigh = None
      averageDeadstockPrice = None
      lastSale = None
      lastSaleSize = None
      salesLast72Hours = None

      def __init__(self, name,shoe,imageUrl,smallImageUrl,thumbUrl,retailPrice,year,
      lowestAsk,lowestAskSize,highestBidSize,deadstockRangeLow,deadstockRangeHigh,
      averageDeadstockPrice,lastSale,lastSaleSize,salesLast72Hours):
        self.name = name
        self.shoe = shoe
        self.imageUrl = imageUrl
        self.smallImageUrl = smallImageUrl
        self.thumbUrl = thumbUrl
        self.retailPrice = retailPrice
        self.year = year
        self.lowestAsk = lowestAsk
        self.lowestAskSize = lowestAskSize
        self.highestBidSize = highestBidSize
        self.deadstockRangeLow = deadstockRangeLow
        self.deadstockRangeHigh = deadstockRangeHigh
        self.averageDeadstockPrice = averageDeadstockPrice
        self.lastSale = lastSale
        self.lastSaleSize = lastSaleSize
        self.salesLast72Hours = salesLast72Hours
