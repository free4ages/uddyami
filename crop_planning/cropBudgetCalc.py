# -*- coding: utf-8 -*-
"""
Created on Sat Jan 02 10:47:48 2021

@author: ajitk
"""

#Inputs
class CropBudgetCalc(object):
    "This is Crop Input Class"
    def __init__(self,**kwargs):
        """
        Acceptable Kwargs
        seed_check, seed_cost, seedling_check, prod_per_plant_av, num_plants_acre, per_plant_cost, sell_price_min,\
        sell_price_max, crop_duration, prod_per_plant_min, prod_per_plant_max, prod_per_acre_min,\
        prod_per_acre_max\
        """
        self.__dict__.update(kwargs)

    def calcProduction(self):
        if (self.prod_per_plant_av and ( self.prod_per_plant_min != 0 and self.prod_per_plant_max != 0 )):
            prod_min =  self.num_plants_acre * self.prod_per_plant_min
            prod_max = self.num_plants_acre * self.prod_per_plant_max
        else:
            prod_min =  self.prod_per_acre_min #in kgs.
            prod_max = self.prod_per_acre_max
        return prod_min, prod_max

    def estRevenue(self):
        prod_min,prod_max = self.calcProduction()
        rev_min = prod_min * self.sell_price_min
        rev_max = prod_max * self.sell_price_max
        rev_norm = (prod_min* self.sell_price_max + prod_max*self.sell_price_min)/2.
        return rev_min,rev_max,rev_norm

    def estSeedingCost(self):
        seeding_cost = 0
        if self.seed_check:
            seeding_cost = self.seed_cost
        elif self.seedling_check:
            seeding_cost = self.per_plant_cost* self.num_plants_acre
        return seeding_cost

    def estPloughingCost(self):
        ploughing_cost = (self.ploughing_bed_cost)*self.crop_duration/12.
        return ploughing_cost

    def estPlantationCost(self):
        plantation_cost = self.plantation_cost
        return plantation_cost

    def estIrrigationCost(self):
        irrigation_cost = self.irrigation_cost
        return irrigation_cost

    def estFertigationCost(self):
        fertigation_cost = 0.
        if self.gobar_check:
            fertigation_cost += self.gobar_cost*self.crop_duration/12.
        if self.fertiliz_bas_check:
            fertigation_cost += self.fertilizer_bas_cost
        if self.fertiliz_ws_check:
            fertigation_cost += self.fertilizer_ws_cost
        if self.vermi_check:
            fertigation_cost += self.vermi_compost_cost
        return fertigation_cost

    def estMulchCost(self):
        if self.mulch_check:
            mulching_cost = (self.mulch_cost + self.mulch_labour_cost)*self.crop_duration/12.
        else:
            mulching_cost = 0.
        return mulching_cost

    def estCropCoverCost(self):
        if self.crop_cover_check:
            crop_cover_cost = self.crop_cover + self.labour_crop_cover + self.wire_cost* self.crop_duration/self.wire_recov_duration
        else:
            crop_cover_cost = 0.
        return crop_cover_cost

    def estAlanCost(self) :
        if self.alan_check:
            alan_cost = self.alan_cost*self.crop_duration/12.
        else:
            alan_cost = 0.
        return alan_cost

    def estStakingCost(self):
        if self.stake_check:
            staking_cost = self.wire_stake + self.wire_thin_tant + self.stake_labour_cost
        else:
            staking_cost = 0.

        return staking_cost

    def estPlantProtectionCost(self):
        pestProtectionCost = self.pesticide_cost
        return pestProtectionCost

    def estWeedingCost(self):
        if self.mulch_check:
            weeding_cost = 0.
        else:
            weeding_cost = self.weeding_cost
        return weeding_cost

    def estCropMgmtCost(self):
        if self.management_check:
            plant_maint_cost = (self.plant_guarding_maintenance_cost + self.management_cost)*self.crop_duration/3.
        else:
           plant_maint_cost = 0.
        return plant_maint_cost

    def estLandLease(self):
        if self.lease_check:
            land_lease = self.land_lease_cost*self.crop_duration/12.
        else:
            land_lease  = 0.
        return land_lease

    def estMarketingCost(self):
        if self.marketing_check:
            marketing_cost = self.marketing_and_harvesting_cost
        else:
            marketing_cost = 0.
        return marketing_cost

    def estMiscellCost(self):
        if self.miscell_check:
            miscell_cost = self.miscell_cost
        else:
            miscell_cost = 0.
        return miscell_cost

    def cropInputCost(self):
        seeding_cost = self.estSeedingCost()
        ploughing_cost = self.estPloughingCost()
        plantation_cost = self.estPlantationCost()
        irrigation_cost = self.estIrrigationCost()
        fertigation_cost = self.estFertigationCost()
        mulching_cost = self.estMulchCost()
        alan_cost = self.estAlanCost()
        staking_cost = self.estStakingCost()
        crop_cover_cost = self.estCropCoverCost()
        plant_protection_cost = self.estPlantProtectionCost()
        weeding_cost = self.estWeedingCost()
        crop_mgmt = self.estCropMgmtCost()
        lease  = self.estLandLease()
        marketing_cost = self.estMarketingCost()
        miscell_cost = self.estMiscellCost()
        total_input_cost = seeding_cost + ploughing_cost + plantation_cost + irrigation_cost + fertigation_cost+\
            mulching_cost + alan_cost + staking_cost + crop_cover_cost + plant_protection_cost +  weeding_cost +  crop_mgmt + lease\
            + marketing_cost + miscell_cost
        return total_input_cost

    def estimateProfit(self):
        rev_min,rev_max,rev_norm = self.estRevenue()
        min_profit = rev_min - self.cropInputCost()
        max_profit = rev_max - self.cropInputCost()
        norm_profit = rev_norm - self.cropInputCost()
        return min_profit,max_profit,norm_profit

    def profitLossData(self):
        min_profit,max_profit,norm_profit = self.estimateProfit()
        rev_min,rev_max,rev_norm = self.estRevenue()
        prod_min, prod_max = self.calcProduction()
        data = [
            ["Normal Profit(INR)" , round(norm_profit)] ,
            ["MAX Profit(INR)" , round(max_profit) ],
            ["MIN Profit(INR)" , round(min_profit) ],
            ["NORMAL Revenue(INR)" , round(rev_norm)] ,
            ["Max Production Per Acre(in Kgs)",  round(prod_max)] ,
            ["Min Production Per Acre(in Kgs)",  round(prod_min)] ,
            ["Total Input Cost(INR)", round(self.cropInputCost())] ,
            ["Min Production Cost per kg(INR)",round(self.cropInputCost()/prod_max)],
            ["Max Production Cost per kg(INR)",round(self.cropInputCost()/prod_min)],
            ["Monthly Normal Profit(INR)" , round(norm_profit/self.crop_duration)] ,
            ["Duration(months) ", self.crop_duration],
        ]
        return data


    def profitLossStatement(self):
        print(self.crop_name)
        min_profit,max_profit,norm_profit = self.estimateProfit()
        print("Normal Profit: Rs." , round(norm_profit) )
        print("Monthly Normal Profit: Rs." , round(norm_profit/self.crop_duration) )
        print("MAX Profit: Rs." , round(max_profit) )
        print("MIN Profit: Rs." , round(min_profit) )
        rev_min,rev_max,rev_norm = self.estRevenue()
        print("NORMAL Revenue: Rs." , round(rev_norm) )
        prod_min, prod_max = self.calcProduction()
        print("Max Production Per Acre: Kgs.",  round(prod_max) )
        print("Min Production Per Acre: Kgs.",  round(prod_min) )
        print("Cost: Rs.", round(self.cropInputCost()) )
        print("Min Production Cost per kg: Rs.",round(self.cropInputCost()/prod_max))
        print("Max Production Cost per kg: Rs.",round(self.cropInputCost()/prod_min))
        print("Duration(months): ", self.crop_duration)

if __name__ == "__main__":
    crop = CropPlan()
    crop.profitLossStatement()

