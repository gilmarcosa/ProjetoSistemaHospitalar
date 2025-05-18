from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers import paciente
from app.routers import profissionalSaude
from app.routers import consulta
from app.routers import receita
from app.routers import prontuario
from app.routers import profissionalInternacao
from app.routers import telemedicina
from app.routers import leito
from app.routers import administracao
from app.routers import internacao
from app.routers import auth

app = FastAPI()

app.include_router(profissionalInternacao.router)
app.include_router(prontuario.router)
app.include_router(receita.router)
app.include_router(consulta.router)
app.include_router(profissionalSaude.router)
app.include_router(paciente.router)
app.include_router(telemedicina.router)
app.include_router(leito.router)
app.include_router(administracao.router)
app.include_router(internacao.router)
app.include_router(auth.router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)