import datetime
import dateutil.parser
from odoo import api,fields, models



class BookRequest(models.Model):
    _name = "bookrequest"

    def action_done(self):
            for rec in self:
                print(rec.name)
                rec.state = 'confirm'
                record6 = self.env['stock'].search([('name','=',rec.name)])
                print(record6.quantity)
                
                for i in record6:
                    q = i.quantity - 1
                if q>-1:  
                    record6.update({
                        'name':rec.name,
                        'quantity':q
                    })
                else:
                    rec.status='pending'
        
    def action_pending(self):
        for rec in self:
            rec.state = 'pending'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_issue(self):
        for rec in self:
            if rec.state == 'confirm':
                self.issue_date = fields.Date.context_today(self)
                rec.state = 'issue'
                return_date = self.issue_date + datetime.timedelta(days=25)
                rec.return_date = return_date
                print(rec.issue_date)
                print(return_date)
            else:
                pass
    
    name = fields.Char("Book Name", readonly=True)
    request_id = fields.Char(string="Request ID", readonly=True, required=True, copy=False, default='New') 
    author = fields.Char("Author",readonly=True)
    edition = fields.Char("Edition",readonly=True)
    publisher = fields.Char("Publisher",readonly=True)
    requestby = fields.Many2one('reader',string="Request By",readonly=True )
    state = fields.Selection(
                [('requested', 'Requested'),
                ('pending', 'Pending'),
                ('confirm', 'Confirm'),
                ('cancel','Cancel'),
                ('issue','Issue')],string='Status',default='requested')
    my_date = fields.Date(
        string='Request Date', default=lambda s: fields.Date.context_today(s))
    issue_date = fields.Date(string='Issue Date')
    return_date = fields.Date(string='Return Date')
    
    
        
    @api.model
    def create(self, vals):
        if vals.get('request_id', 'New') == 'New':
            vals['request_id'] = self.env['ir.sequence'].next_by_code('bookrequest') or 'New'
        result = super(BookRequest, self).create(vals)
        return result

    
    @api.onchange('issue_date')
    def request_date(self):
        print("...........................>>>>>>>..................>>>>>>>>>>.")
        for record in self:
            return_date = record.issue_date + datetime.timedelta(days=25)
            record.return_date = return_date
            print(record.return_date)
    
    
