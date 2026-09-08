import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add back button in HTML
back_btn = """
    <button id="btn-volver" class="ui-element">
        <i class="bi bi-arrow-left"></i> Volver a la órbita
    </button>
"""
html = html.replace('<footer class="ui-element footer">', back_btn + '\n    <footer class="ui-element footer">')

# 2. Update CSS for content-display to be fixed and centered, and add btn-volver css
css_old = """.content-display {
            position: absolute;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s cubic-bezier(0.19, 1, 0.22, 1), opacity 0.4s ease-out, padding 0.4s ease-out;
            padding: 0;
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            z-index: 150;
            box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        }

        .dropdown.active .content-display {
            max-height: 600px;
            padding: 1.5rem;
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
        }"""

css_new = """.content-display {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -40%) scale(0.9);
            width: min(90vw, 800px);
            max-height: 80vh;
            overflow-y: auto;
            transition: all 0.6s cubic-bezier(0.19, 1, 0.22, 1);
            padding: 2rem;
            background: rgba(30, 30, 30, 0.5);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            z-index: 150;
            box-shadow: 0 20px 50px rgba(0,0,0,0.6);
        }

        .content-display.active {
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
            transform: translate(-50%, -50%) scale(1);
        }
        
        .dropdown {
            position: fixed;
            z-index: 100;
            padding: 3vw;
        }

        #btn-volver {
            bottom: 5%;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: var(--light-grey);
            padding: 0.8rem 1.5rem;
            border-radius: 30px;
            cursor: pointer;
            font-family: 'Space Mono', monospace;
            font-size: 1rem;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 200;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        #btn-volver:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateX(-50%) scale(1.05);
        }
        
        #btn-volver.visible {
            opacity: 1;
            visibility: visible;
        }
        
        .star-trigger {
            transition: all 0.5s ease;
        }
        .star-trigger.hidden {
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
        }
"""
html = html.replace(css_old, css_new)

# 3. Clean up old specific dropdown positioning (since content-display is fixed globally now)
# We need to remove the top/left positioning for .content-display inside specific dropdowns
css_dropdown_specifics = """        #proyectos-dropdown .content-display {
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            width: min(90vw, 600px);
            max-width: 600px;
        }

        #info-dropdown {
            top: 50%;
            left: 10%;
        }

        #info-dropdown .content-display {
            top: 40%;
            left: 20%;
            transform: translate(-20%, -40%);
            width: 800px;
            max-width: 90vw;
            margin-top: 60px;
        }

        #contacto-dropdown {
            top: 40%;
            right: 10%;
        }

        #contacto-dropdown .content-display {
            top: 100%;
            right: 0;
            width: 300px;
            max-width: 350px;
            text-align: center;
        }"""
html = html.replace(css_dropdown_specifics, """        #info-dropdown {
            top: 50%;
            left: 10%;
        }

        #contacto-dropdown {
            top: 40%;
            right: 10%;
        }""")

# 4. Mobile css fixes
css_mobile_old = """            #info-dropdown .content-display { display: none !important; }
            #proyectos-dropdown { top: 50%; left: 50%; transform: translate(-50%, -50%); }
            #contacto-dropdown { top: 20%; right: 5%; }
            #contacto-dropdown .content-display { display: none !important; }"""

css_mobile_new = """            #proyectos-dropdown { top: 75%; left: 50%; transform: translate(-50%, -50%); }
            #contacto-dropdown { top: 20%; right: 5%; }"""
html = html.replace(css_mobile_old, css_mobile_new)

html = html.replace(".content-display {\n                display: none !important;\n            }", "")

# 5. JS rewrite for camera movement and interaction
js_old_start = "            const starTriggers = document.querySelectorAll('.star-trigger');"
js_old_end = "            const clock = new Clock();"

js_new = """            const starTriggers = document.querySelectorAll('.star-trigger');
            const btnVolver = document.getElementById('btn-volver');
            const iconParticleSystems = new Map();
            
            // --- NAVEGACIÓN 3D ---
            const views = {
                home:      { pos: new Vector3(0, 0, 5),   look: new Vector3(0, 0, 0) },
                proyectos: { pos: new Vector3(0, -15, 8), look: new Vector3(0, -30, -5) },
                info:      { pos: new Vector3(-20, 0, 8), look: new Vector3(-40, 0, -5) },
                contacto:  { pos: new Vector3(20, 0, 8),  look: new Vector3(40, 0, -5) }
            };
            
            let currentView = 'home';
            const targetCameraPos = new Vector3().copy(views.home.pos);
            const targetCameraLook = new Vector3().copy(views.home.look);
            const currentCameraLook = new Vector3().copy(views.home.look);
            
            function navigateTo(viewName) {
                currentView = viewName;
                const view = views[viewName];
                targetCameraPos.copy(view.pos);
                targetCameraLook.copy(view.look);
                
                // Hide all panels and active triggers
                document.querySelectorAll('.content-display').forEach(el => el.classList.remove('active'));
                
                if (viewName === 'home') {
                    btnVolver.classList.remove('visible');
                    // Show triggers
                    starTriggers.forEach(el => {
                        el.classList.remove('hidden', 'active');
                        const data = iconParticleSystems.get(el);
                        if(data) data.active = false;
                    });
                } else {
                    // Hide triggers
                    starTriggers.forEach(el => el.classList.add('hidden'));
                    // Show target panel with a delay for the camera movement
                    setTimeout(() => {
                        if (currentView === viewName) {
                            document.getElementById(`${viewName}-content`).classList.add('active');
                            btnVolver.classList.add('visible');
                        }
                    }, 600);
                }
            }

            btnVolver.addEventListener('click', () => navigateTo('home'));

            starTriggers.forEach(trigger => {
                const particleCount = 15;
                const positions = new Float32Array(particleCount * 3).fill(0);
                const velocities = new Float32Array(particleCount * 3);
                const lifetimes = new Float32Array(particleCount).fill(0);
                for(let i = 0; i < velocities.length; i++) velocities[i] = (Math.random() - 0.5) * 0.2;
                const geometry = new BufferGeometry();
                geometry.setAttribute('position', new Float32BufferAttribute(positions, 3));
                geometry.setAttribute('velocity', new Float32BufferAttribute(velocities, 3));
                geometry.setAttribute('lifetime', new Float32BufferAttribute(lifetimes, 1));
                const material = new PointsMaterial({ 
                    color: 0xffffff, 
                    size: 0.15, 
                    map: circleTexture,
                    sizeAttenuation: true, 
                    transparent: true, 
                    opacity: 0.9, 
                    blending: AdditiveBlending,
                    depthWrite: false
                });
                const particleSystem = new Points(geometry, material);
                particleSystem.visible = false;
                scene.add(particleSystem);
                iconParticleSystems.set(trigger, { system: particleSystem, active: false });
            });

            function updateIconParticles() {
                if (currentView !== 'home') return;
                iconParticleSystems.forEach(({ system, active }, trigger) => {
                    if (!active || !trigger.offsetParent) return;
                    const { position, velocity, lifetime } = system.geometry.attributes;
                    for (let i = 0; i < lifetime.array.length; i++) {
                        if (lifetime.array[i] > 0) {
                            position.array[i * 3] += velocity.array[i * 3] * 0.01;
                            position.array[i * 3 + 1] += velocity.array[i * 3 + 1] * 0.01;
                            position.array[i * 3 + 2] += velocity.array[i * 3 + 2] * 0.01;
                            lifetime.array[i] -= 0.01;
                            if (lifetime.array[i] <= 0) {
                                position.array[i * 3] = position.array[i * 3 + 1] = position.array[i * 3 + 2] = 0;
                                lifetime.array[i] = 0;
                            }
                        } else if (Math.random() < 0.03) {
                            position.array[i * 3] = position.array[i * 3 + 1] = position.array[i * 3 + 2] = 0;
                            velocity.array[i * 3] = (Math.random() - 0.5) * 0.2;
                            velocity.array[i * 3 + 1] = (Math.random() - 0.5) * 0.2;
                            velocity.array[i * 3 + 2] = (Math.random() - 0.5) * 0.2;
                            lifetime.array[i] = 1;
                        }
                    }
                    position.needsUpdate = lifetime.needsUpdate = true;
                    
                    const rect = trigger.getBoundingClientRect();
                    const x = (rect.left + rect.width / 2) / window.innerWidth * 2 - 1;
                    const y = -(rect.top + rect.height / 2) / window.innerHeight * 2 + 1;
                    
                    // Simple unproject mapping since we are at home
                    const vector = new Vector3(x, y, 0).unproject(camera);
                    const dir = vector.sub(camera.position).normalize();
                    const distance = -camera.position.z / dir.z;
                    system.position.copy(camera.position.clone().add(dir.multiplyScalar(distance)));
                });
            }

            const tooltip = document.getElementById('project-tooltip');
            const tooltipImg = document.getElementById('tooltip-img');
            const tooltipDesc = document.getElementById('tooltip-desc');
            const tooltipDemo = document.getElementById('tooltip-demo');
            const tooltipRepo = document.getElementById('tooltip-repo');
            const isMobile = window.innerWidth <= 768;
            
            function handleProjectClick(e) {
                e.preventDefault();
                e.stopPropagation();
                const link = e.target.closest('.project-link');
                if (!link) return;
                tooltipImg.src = link.dataset.img;
                tooltipDesc.textContent = link.dataset.description;
                tooltipDemo.href = link.dataset.demo || '#';
                tooltipRepo.href = link.dataset.repo || '#';
                tooltipDemo.classList.toggle('hidden', !link.dataset.demo);
                tooltip.classList.add('visible');
                tooltip.setAttribute('aria-hidden', 'false');
            }

            starTriggers.forEach(trigger => {
                trigger.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const sectionName = trigger.closest('.dropdown').id.replace('-dropdown', '');
                    navigateTo(sectionName);
                });
                
                if (!isMobile) {
                    trigger.addEventListener('mouseenter', () => {
                        if (currentView === 'home') {
                            const data = iconParticleSystems.get(trigger);
                            if (data) {
                                data.active = data.system.visible = true;
                                trigger.classList.add('active');
                            }
                        }
                    });
                    trigger.addEventListener('mouseleave', () => {
                        if (currentView === 'home') {
                            const data = iconParticleSystems.get(trigger);
                            if (data) {
                                data.active = data.system.visible = false;
                                trigger.classList.remove('active');
                            }
                        }
                    });
                }
            });

            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    if (tooltip.classList.contains('visible')) {
                        tooltip.classList.remove('visible');
                    } else if (currentView !== 'home') {
                        navigateTo('home');
                    }
                }
            });

            document.querySelectorAll('.project-link').forEach(link => {
                link.addEventListener('click', handleProjectClick);
            });

            document.addEventListener('click', (e) => {
                if (!tooltip.contains(e.target) && !e.target.closest('.project-link')) {
                    tooltip.classList.remove('visible');
                    tooltip.setAttribute('aria-hidden', 'true');
                }
            });

            const mouse = new Vector2();
            window.addEventListener('mousemove', (e) => {
                mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
                mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;
            });
            
            const clock = new Clock();"""

import re
html = html[:html.find(js_old_start)] + js_new + html[html.find(js_old_end) + len("            const clock = new Clock();"):]

# Update the animate loop to handle camera lerping
js_animate_old = """            function animate() {
                const elapsedTime = clock.getElapsedTime();
                backgroundParticles.rotation.y = elapsedTime * 0.05;
                backgroundParticles.rotation.x = elapsedTime * 0.02;
                camera.position.x += (mouse.x * 0.5 - camera.position.x) * 0.02;
                camera.position.y += (mouse.y * 0.5 - camera.position.y) * 0.02;
                camera.lookAt(scene.position);
                updateIconParticles();
                renderer.render(scene, camera);
                requestAnimationFrame(animate);
            }"""

js_animate_new = """            function animate() {
                const elapsedTime = clock.getElapsedTime();
                backgroundParticles.rotation.y = elapsedTime * 0.02;
                backgroundParticles.rotation.x = elapsedTime * 0.01;
                
                // Suave movimiento de cámara hacia el objetivo (Lerp)
                camera.position.lerp(targetCameraPos, 0.04);
                currentCameraLook.lerp(targetCameraLook, 0.04);
                
                // Añadir sutil efecto parallax con el ratón sobre la vista actual
                const mouseOffset = new Vector3(mouse.x * 0.5, mouse.y * 0.5, 0);
                const finalLookAt = currentCameraLook.clone().add(mouseOffset);
                
                camera.lookAt(finalLookAt);
                
                updateIconParticles();
                renderer.render(scene, camera);
                requestAnimationFrame(animate);
            }"""
html = html.replace(js_animate_old, js_animate_new)

# Remove the old modal HTML code since we removed toggleSection logic for mobile
# Instead of modal, mobile will just show the fixed panel
modal_html = """    <div class="modal-overlay" id="modal-overlay">
        <div class="modal-content">
            <button class="modal-close" aria-label="Cerrar modal">×</button>
            <div id="modal-body"></div>
        </div>
    </div>"""
html = html.replace(modal_html, "")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

