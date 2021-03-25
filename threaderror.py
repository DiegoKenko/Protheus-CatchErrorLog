import sys
import connDB


class threaderror:
    def __init__(self, full: str):
        mark_i_usuario = full.find(',') + 1
        mark_i_titulo = full.find(')') + 25
        mark_i_build = full.find('[build')
        mark_i_ambiente = full.find('[environment')
        mark_i_thread = full.find('[thread')
        mark_i_dbthread = full.find('[dbthread')
        mark_i_dbversion = full.find('[dbversion')
        mark_i_dbapibuild = full.find('[dbapibuild')
        mark_i_localfiles = full.find('[localfiles')
        mark_i_remark = full.find('[remark')
        mark_i_empresa = full.find('Emp ') + 4
        mark_i_data = full.find(')') + 4
        mark_i_hora = full.find(')') + 14
        mark_i_porta = full.find('[porta') + 7
        mark_f_usuario = full.find(']') + 17
        mark_f_titulo = full.find('[build') - 2
        mark_f_build = full.find('[environment')
        mark_f_ambiente = full.find('[thread')
        mark_f_thread = full.find('[thread') + 15
        mark_f_dbthread = full.find('[dbversion')
        mark_f_dbversion = full.find('[dbapibuild')
        mark_f_dbapibuild = full.find('[dbarch:')
        mark_f_localfiles = full.find('[remark')
        mark_f_remark = full.find('Variables in use')
        mark_f_empresa = full.find('Emp ') + 11
        mark_f_data = full.find(')') + 14
        mark_f_hora = full.find(')') + 27
        mark_f_porta = full.find('[porta') + 12
        self.tipo = 'THREAD ERROR'
        self.usuario = full[mark_i_usuario:mark_f_usuario].replace(
            ',', '').strip()
        self.titulo = full[mark_i_titulo:mark_f_titulo].strip()
        self.build = full[mark_i_build:mark_f_build].replace(
            '[', '').replace(']', '').replace('build', '').replace(':', '').strip()
        self.ambiente = full[mark_i_ambiente:mark_f_ambiente].replace(
            '[', '').replace(']', '').replace('environment', '').replace(':', '').strip()
        self.thread = full[mark_i_thread:mark_f_thread].replace(
            '[', '').replace(']', '').replace('thread', '').replace(':', '').strip()
        self.dbthread = full[mark_i_dbthread:mark_f_dbthread].replace(
            '[', '').replace(']', '').replace('dbthread', '').replace(':', '').strip()
        self.dbversion = full[mark_i_dbversion:mark_f_dbversion].replace(
            '[', '').replace(']', '').replace('dbversion', '').replace(':', '').strip()
        self.dbapibuild = full[mark_i_dbapibuild:mark_f_dbapibuild].replace(
            '[', '').replace(']', '').replace('dbapibuild', '').replace(':', '').strip()
        self.localfiles = full[mark_i_localfiles:mark_f_localfiles].replace(
            '[', '').replace(']', '').replace('localfiles', '').replace(':', '').strip()
        self.remark = full[mark_i_remark:mark_f_remark].replace(
            '[', '').replace(']', '').replace('remark', '').replace(':', '').strip()
        self.empresa = full[mark_i_empresa:mark_f_empresa].replace(
            '[', '').replace(']', '').replace('remark', '').replace(':', '').strip()
        self.data = full[mark_i_data:mark_f_data].strip()
        self.hora = full[mark_i_hora:mark_f_hora].strip()
        self.porta = full[mark_i_porta:mark_f_porta].strip()

    def Cria(self):
        cnxn = connDB.Conecta()
        cursor = cnxn.cursor()
        cursor.execute(
            "INSERT INTO LOGREADER(TIPO,USUARIO,TITULO,BUILD,AMBIENTE,THREAD,DBTHREAD,DBVERSION,DBAPIBUILD,LOCALFILES,REMARK,EMPRESA,DATA,HORA,PORTA) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", self.tipo, self.usuario, self.titulo, self.build, self.ambiente, self.thread, self.dbthread, self.dbversion, self.dbapibuild, self.localfiles, self.remark, self.empresa,self.data,self.hora,self.porta)
        cnxn.commit()
