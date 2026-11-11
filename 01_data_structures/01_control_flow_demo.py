# pylint: disable = C0103, W0311
"============ if, match, wihle ============"

alter = int(input(" wie alt bist du? "))
if alter >= 18:
    print("Treten Sie ein!")
elif alter >= 14:
    print("Aber nur in Begleitung Deiner Eltern darfst du rein")
else:
    print("Du komst hier nicht rein!")
