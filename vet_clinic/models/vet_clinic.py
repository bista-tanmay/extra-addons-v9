from openerp import models, fields, api, _


class vet_clinic_animal(models.Model):
    _name = 'vet.clinic.animal'

    name = fields.Char('Name',required=True)
    birth_date = fields.Date('Birth Date')
    classification_id = fields.Many2one('vet.clinic.classification', 'Classification',required=True)
    breed_id = fields.Many2one('vet.clinic.breed', 'Breed')
    labels_ids = fields.Many2many('vet.clinic.labels', 'animal_labels_rel', 'animal_id', 'labels_id', string='Labels')
    history = fields.Text('History')
    res_partner_id = fields.Many2one('res.partner', 'Owner')
    image = fields.Binary('Image')
    animal_vacination_ids = fields.One2many('vet.clinic.animal.vacination', 'animal_id', string='Vacinations')

class VetClinicAnimalVacination(models.Model):
    _name = 'vet.clinic.animal.vacination'
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.product','Vaccination')
    due_date = fields.Date('Due Date')
    date_performed = fields.Date('Date Performed')
    animal_id = fields.Many2one('vet.clinic.animal','Animal')

class vet_clinic_classification(models.Model):
    _name = 'vet.clinic.classification'

    name = fields.Char('Name')
    breed_ids = fields.One2many('vet.clinic.breed', 'classification_id', string='Breed')


class vet_clinic_breed(models.Model):
    _name = 'vet.clinic.breed'

    name = fields.Char('Name')
    classification_id = fields.Many2one('vet.clinic.classification','Classification')


class vet_clinic_labels(models.Model):
    _name = 'vet.clinic.labels'

    name = fields.Char('Name')


class vet_clinic_res_partner(models.Model):
    _inherit = 'res.partner'

    animal_ids = fields.One2many('vet.clinic.animal', 'res_partner_id', string='Pets')

