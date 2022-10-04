""" File untuk kelas Error """

class LoginError(Exception):
    def __init__(self, *args):
        """
        Kelas LoginError untuk menampung kegagalan login akibat
        data user yang invalid.
        Args (optional) dapat berupa sebuah message error.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None


class RegisterError(Exception):
    def __init__(self, *args):
        """
        Kelas RegisterError untuk menampung kegagalan register akibat
        input data yang invalid.
        Args (optional) dapat berupa sebuah message error.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

class KelolaInformasiParkiranError(Exception):
    def __init__(self, *args):
        """
        Kelas KelolaInformasiParkiranError untuk menampung kegagalan
        memperbarui informasi parkiran pada database karena
        terdapat input yang tidak valid dari pengguna
        Args (optional) dapat berupa sebuah message error.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None


class HitungBiayaError(Exception):
    def __init__(self, *args):
        """
        Kelas KelolaInformasiParkiranError untuk menampung kegagalan
        memperbarui informasi parkiran pada database karena
        terdapat input yang tidak valid dari pengguna
        Args (optional) dapat berupa sebuah message error.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

class CatatKendaraanMasukError(Exception):
    def __init__(self, *args):
        """
        Kelas KelolaInformasiParkiranError untuk menampung kegagalan
        memperbarui informasi parkiran pada database karena
        terdapat input yang tidak valid dari pengguna
        Args (optional) dapat berupa sebuah message error.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

class CatatKendaraanKeluarError(Exception):
    def __init__(self, *args):
        """
        Kelas KelolaInformasiParkiranError untuk menampung kegagalan
        memperbarui informasi parkiran pada database karena
        terdapat input yang tidak valid dari pengguna
        Args (optional) dapat berupa sebuah message error.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None
        