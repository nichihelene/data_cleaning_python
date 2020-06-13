import whyqd as _w

schema = _w.Schema()

details = {
   "name": "Gender_Empowerment_Measure_Per_Country_Table_29_Nojh",
   "title": "Gender empowerment measure and achieving equality for all women and men ",
   "description": "Database that ranks countries based on the gender empowerment measure taken by them  in achieving "
                  "equality for all women and men ",
}


fields = [
      {
        "name": "HDI_rank",
        "title": "HDI rank",
        "type": "integer",
        "description": "HDI rank of the countries determined on the basis of GEM values",
        "constraints": {
          "minimum": 1,
          "maximum": 177,
          "unique": True
        }
      },
      {
        "name": "Hum_dev_level",
        "title": "Human Development Level(HDL)",
        "type": "string",
        "description": "Human Development Level of all the countries from those who have the highest human development "
                       "level to those who have  the lowest human development and it is determined on the basis of "
                       "GEM values",
        "constraints": {
          "category": [
              {"name": "High"},
              {"name": "Medium"},
              {"name": "Low"}
          ]
        }
      },
      {
        "name": "Country_name",
        "title": "Country Name",
        "type": "string",
        "description": "Name  of the countries",
        "constraints": {
          "maximum": 4,
          "required": True
        }
      },
      {
        "name": "GEM_rank",
        "title": "Gender empowerment measure (GEM) Rank  ",
        "type": "integer",
        "description": "Gender empowerment measure (GEM) Rank of the countries",
        "constraints": {
          "minimum": 1
        }
      },
      {
        "name": "GEM_value ",
        "title": "Gender empowerment measure (GEM) Value",
        "type": "number",
        "description": "Gender empowerment measure (GEM) Value of the countries",
        "constraints": {
          "minimum": 0
        }
      },
      {
        "name": "Seats_parlia_wom",
        "title": "Seats in parliament held by womena (% of total)",
        "type": "number",
        "description": "Seats in parliament held by womena (% of total) ;percentage  calculated on the basis of data "
                       "on parliamentary seats from IPU 2007c",
        "constraints": {
          "minimum": 0
        }
      },
      {
        "name": "Fem _le_snr_offi_mana",
        "title": "Female legislators,senior officials and managersb  (% of total)",
        "type": "integer",
        "description": "percentage of Female legislators,senior officials and managersb calculated on the basis of "
                       "occupational data from ILO 2007b ",
        "constraints": {
          "minimum": 1
        }
      },
      {
        "name": "Fem_profes_techn_work",
        "title": "Female professional and technical workersb  (% of total)",
        "type": "integer",
        "description": "percentage of the female professional and technical worked calculated on the basis of "
                       "occupational data from ILO 2007b.  ",
        "constraints": {
          "minimum": 10
        }
      },
      {
        "name": "Ratio_esti_ fem_male_earn_ incom",
        "title": "Ratio of estimated  female to male earned incomec",
        "type": "number",
        "description": "Ratio of estimated  female to male earned incomec calculated on the basis of data in columns "
                       "9 and 10 of Table 28 ",
        "constraints": {
          "minimum": 0
        }
      }
    ]


if __name__ == "__main__":

    for field in fields:
        schema.set_field(**field)

    print(schema.default_field_settings("string"))
