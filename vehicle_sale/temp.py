partner = request.env['employee.information'].sudo().create({
 'name': post.get('name'),
 'mobile_no': post.get('mobile_no'),
 'email':post.get('email'),
 'date_of_birth':post.get('date_of_birth'),
 # 'resume': value,
 'company_name':post.get('company_name'),
 'job_info':post.get('job_info'),
 })
 
 attached_files = request.httprequest.files.getlist('attachment')
 for attachment in attached_files:
 attached_file = attachment.read()
 attachment = request.env['ir.attachment'].sudo().create({
 'name': attachment.filename,
 'res_model': 'employee.information',
 'res_id': partner,
 'type': 'binary',
 # 'name': attachment.filename,
 'datas': base64.encodestring(attached_file),
 })
 return request.redirect('/')