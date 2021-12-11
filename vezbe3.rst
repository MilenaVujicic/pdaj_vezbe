Merenje performansi izvršavanja programa
========================================

 - Biblioteka time:
    funckija **time.time()** podatak o trenutnom vremenu. Merenje vremena računanjem razlike između početka i kraja izvršavanja funkcije/programa (U sekundama).

 - Biblioteka tracemalloc:
    merenje utrošene radne memorije tokom izvršavanja funkcije/programa. **tracemalloc.start()** funkcija označava početak merenja potrošnje ram-a. **tracemalloc.get_traced_memory()** vraća utrošen od trenutka poziva funkcije **tracemalloc.start()**.
    **tracemalloc.stop()** zaustavlja merenje.


Biblioteka multiprocessing
==========================
Dokumentacija: https://docs.python.org/3/library/multiprocessing.html
