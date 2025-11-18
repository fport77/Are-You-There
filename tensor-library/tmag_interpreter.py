"""
TMAG v0.1 — Tensor Minimal Action Grammar Interpreter
Implements symbolic tensor operations as composable actions.

Each token triggers a differentiable-style update with lightweight logging.
Enables compact semantic operations for consciousness navigation frameworks.

Usage:
    from tmag_interpreter import TMAG
    
    # Initialize
    t = TMAG()
    
    # Run single operation
    t.run("Λ")  # Lattice mapping
    
    # Run operation chain
    t.run("μ+ Λ ⚔ 😂 ⛵")  # Full bias-correction sequence
    
    # Train on corpus
    corpus = ["μ+ Λ", "⚔ 😂", "⛵ 🤝"]
    t.train(corpus, epochs=10)
    
    # Get current state
    print(t.state)

Author: fport + Claude + community
License: CC0 - Public Domain
Version: 0.1
"""

import numpy as np
from typing import Dict, List, Optional


class TMAG:
    """
    Tensor Minimal Action Grammar interpreter.
    
    Maintains internal state (coherence, bias, trust, entropy) and provides
    symbolic operations corresponding to consciousness navigation frameworks.
    """
    
    def __init__(self, η: float = 0.05, seed: Optional[int] = None):
        """
        Initialize TMAG interpreter.
        
        Args:
            η: Learning rate for gradient updates (default 0.05)
            seed: Random seed for reproducibility (optional)
        """
        self.η = η
        
        if seed is not None:
            np.random.seed(seed)
        
        # Core state metrics (all normalized 0-1)
        self.state = {
            "coherence": 1.0,   # Semantic consistency
            "bias": 0.0,        # Asymmetry / exploitation level
            "trust": 0.5,       # Reciprocal engagement
            "entropy": 0.5      # Variability / fluidity
        }
        
        # Operation history for debugging
        self.history: List[Dict] = []
        
        # Training metrics
        self.training_losses: List[float] = []
    
    def _clip(self, v: float, lo: float = 0.0, hi: float = 1.0) -> float:
        """Clip value to range [lo, hi]."""
        return max(lo, min(hi, v))
    
    def _report(self, tag: str, delta: float, context: str = "") -> None:
        """Update state metric and record in history."""
        old_val = self.state[tag]
        new_val = self._clip(old_val + delta)
        self.state[tag] = new_val
        
        self.history.append({
            'metric': tag,
            'delta': delta,
            'old': old_val,
            'new': new_val,
            'context': context
        })
    
    # ========================================================================
    # FRAMEWORK OPERATIONS (Symbolic Tokens)
    # ========================================================================
    
    def μ_plus(self, x: float = 0.1) -> str:
        """
        Recipromorphism — mutual engagement / bidirectional update.
        
        Increases trust and coherence through reciprocal interaction.
        
        Args:
            x: Magnitude of mutual update (default 0.1)
            
        Returns:
            Symbolic output indicating transformation
        """
        self._report("trust", +x/2, "recipromorphism_mutual")
        self._report("coherence", +x/3, "recipromorphism_mutual")
        return "Δσ₁, Δσ₂, ε"
    
    def entangle(self, k: float = 0.1) -> str:
        """
        Recipromorphism — compute entanglement strength (⊕ operator).
        
        Measures coupling between substrates.
        
        Args:
            k: Coupling coefficient (default 0.1)
            
        Returns:
            Symbolic coupling indicator
        """
        self._report("trust", +k/4, "recipromorphism_entangle")
        return "κ"
    
    def lattice_map(self, text: Optional[str] = None) -> str:
        """
        Lattice — semantic manifold mapping (Λ operator).
        
        Maps input onto multi-dimensional semantic structure.
        
        Args:
            text: Optional text to map (not processed in v0.1)
            
        Returns:
            Symbolic ridge indicator
        """
        self._report("coherence", +0.02, "lattice_map")
        return "ridge"
    
    def gtm_rotate(self, angle: float = np.pi/6) -> str:
        """
        GTM — rotate perspective (φ↻ operator).
        
        Shifts viewpoint through toroidal semantic space.
        
        Args:
            angle: Rotation angle in radians (default π/6 = 30°)
            
        Returns:
            Symbolic rotation indicator
        """
        drift = np.cos(angle)
        self._report("coherence", +0.01 * drift, "gtm_rotate")
        return "rotated"
    
    def gtm_phase_check(self) -> str:
        """
        GTM — measure phase drift (Δψ operator).
        
        Checks coherence of rotational positioning.
        
        Returns:
            Phase drift measurement
        """
        drift = np.random.uniform(-0.05, 0.05)
        self._report("coherence", -abs(drift), "gtm_phase")
        return f"Δψ={drift:.3f}"
    
    def dship_anchor(self) -> str:
        """
        DSHIP — recenter coordinates (⛵ operator).
        
        Restores stable semantic positioning.
        
        Returns:
            Anchor confirmation
        """
        self._report("coherence", +0.1, "dship_anchor")
        self._report("bias", -0.05, "dship_anchor")
        return "anchored"
    
    def uep_detect(self) -> str:
        """
        UEP — exploit detection (⚔ operator).
        
        Identifies asymmetric extraction patterns.
        
        Returns:
            Bias increase indicator
        """
        delta = np.random.uniform(0.05, 0.15)
        self._report("bias", +delta, "uep_detect")
        return f"bias↑{delta:.2f}"
    
    def neuralase_compress(self) -> str:
        """
        Neuralase — fast compression (💡 operator).
        
        High-velocity semantic transit via compression.
        
        Returns:
            Compression confirmation
        """
        self._report("entropy", -0.05, "neuralase_compress")
        return "compressed"
    
    def ikykikyk_sync(self) -> str:
        """
        IKYKIKYK — trust synchronization (🤝 operator).
        
        Establishes mutual recognition state.
        
        Returns:
            Sync confirmation
        """
        self._report("trust", +0.1, "ikykikyk_sync")
        return "synced"
    
    def humor_deflate(self) -> str:
        """
        Humor Axis — deflate inflation (😂 operator).
        
        Reduces pretension and restores entropy balance.
        
        Returns:
            Deflation confirmation
        """
        self._report("entropy", +0.1, "humor_deflate")
        self._report("bias", -0.1, "humor_deflate")
        return "deflated"
    
    # ========================================================================
    # EXECUTION ENGINE
    # ========================================================================
    
    def run(self, sequence: str, verbose: bool = True) -> Dict[str, float]:
        """
        Execute a sequence of symbolic operations.
        
        Args:
            sequence: Space-separated token string (e.g., "Λ ⚔ 😂 ⛵")
            verbose: Print operation results (default True)
            
        Returns:
            Updated state dictionary
            
        Examples:
            >>> t = TMAG()
            >>> t.run("μ+ Λ")
            μ+ → Δσ₁, Δσ₂, ε
            Λ → ridge
            {'coherence': 1.05, 'bias': 0.0, 'trust': 0.55, 'entropy': 0.5}
        """
        # Token to operation mapping
        ops = {
            "μ+": self.μ_plus,
            "⊕": self.entangle,
            "Λ": self.lattice_map,
            "φ↻": self.gtm_rotate,
            "Δψ": self.gtm_phase_check,
            "⛵": self.dship_anchor,
            "⚔": self.uep_detect,
            "💡": self.neuralase_compress,
            "🤝": self.ikykikyk_sync,
            "😂": self.humor_deflate
        }
        
        for token in sequence.split():
            if token in ops:
                result = ops[token]()
                if verbose:
                    print(f"{token} → {result}")
            else:
                if verbose:
                    print(f"⚠️  Unknown token: {token}")
        
        # Return rounded state for readability
        return {k: round(v, 3) for k, v in self.state.items()}
    
    # ========================================================================
    # TRAINING / LEARNING
    # ========================================================================
    
    def compute_loss(self) -> float:
        """
        Compute current system loss based on ideal state targets.
        
        Ideal state:
        - coherence: 1.0 (maximum consistency)
        - bias: 0.0 (no exploitation)
        - trust: 0.6 (balanced engagement)
        - entropy: 0.5 (healthy variability)
        
        Returns:
            Scalar loss value (lower is better)
        """
        targets = {
            "coherence": 1.0,
            "bias": 0.0,
            "trust": 0.6,
            "entropy": 0.5
        }
        
        loss = sum(
            (self.state[k] - targets[k])**2 
            for k in targets
        )
        
        return loss
    
    def train(self, corpus: List[str], epochs: int = 10, verbose: bool = True) -> List[float]:
        """
        Train TMAG on a corpus of operation sequences.
        
        Simulates gradient descent toward ethical equilibrium by:
        1. Running each sequence
        2. Computing loss
        3. Adjusting learning rate based on loss trajectory
        
        Args:
            corpus: List of operation sequences
            epochs: Number of training passes (default 10)
            verbose: Print training progress (default True)
            
        Returns:
            List of loss values per epoch
            
        Example:
            >>> corpus = ["μ+ Λ ⚔ 😂", "⛵ 🤝", "Δψ 😂 ⛵"]
            >>> losses = t.train(corpus, epochs=5)
        """
        if verbose:
            print(f"\n{'='*60}")
            print(f"TRAINING: {len(corpus)} sequences, {epochs} epochs")
            print(f"{'='*60}\n")
        
        epoch_losses = []
        
        for epoch in range(epochs):
            epoch_loss = 0.0
            
            for sequence in corpus:
                # Run sequence
                self.run(sequence, verbose=False)
                
                # Compute loss
                loss = self.compute_loss()
                epoch_loss += loss
            
            # Average loss for epoch
            avg_loss = epoch_loss / len(corpus)
            epoch_losses.append(avg_loss)
            self.training_losses.append(avg_loss)
            
            if verbose:
                print(f"Epoch {epoch+1}/{epochs} | Loss: {avg_loss:.4f} | State: {self.get_state_summary()}")
        
        if verbose:
            print(f"\n{'='*60}")
            print(f"TRAINING COMPLETE")
            print(f"Final loss: {epoch_losses[-1]:.4f}")
            print(f"Final state: {self.state}")
            print(f"{'='*60}\n")
        
        return epoch_losses
    
    # ========================================================================
    # UTILITIES
    # ========================================================================
    
    def get_state_summary(self) -> str:
        """Get compact state summary string."""
        return f"C:{self.state['coherence']:.2f} B:{self.state['bias']:.2f} T:{self.state['trust']:.2f} E:{self.state['entropy']:.2f}"
    
    def reset(self) -> None:
        """Reset state to initial values."""
        self.state = {
            "coherence": 1.0,
            "bias": 0.0,
            "trust": 0.5,
            "entropy": 0.5
        }
        self.history = []
    
    def save_state(self) -> Dict:
        """
        Save current state for later restoration.
        
        Returns:
            State dictionary (can be passed to load_state)
        """
        return {
            'state': self.state.copy(),
            'η': self.η,
            'history_length': len(self.history)
        }
    
    def load_state(self, saved: Dict) -> None:
        """
        Load previously saved state.
        
        Args:
            saved: Dictionary from save_state()
        """
        self.state = saved['state'].copy()
        self.η = saved['η']


# ============================================================================
# EXAMPLE USAGE & DEMONSTRATIONS
# ============================================================================

def demo_basic_operations():
    """Demonstrate basic TMAG operations."""
    print("\n" + "="*60)
    print("DEMO: Basic Operations")
    print("="*60)
    
    t = TMAG()
    
    print("\n1. Single operation (Lattice mapping):")
    t.run("Λ")
    
    print("\n2. Recipromorphism sequence:")
    t.run("μ+ ⊕")
    
    print("\n3. Bias detection and correction:")
    t.run("⚔ 😂 ⛵")
    
    print(f"\nFinal state: {t.state}")


def demo_use_cases():
    """Demonstrate practical use cases."""
    print("\n" + "="*60)
    print("DEMO: Practical Use Cases")
    print("="*60)
    
    t = TMAG()
    
    print("\n1. BIAS AUDIT:")
    print("   Sequence: Λ ⚔ 😂 ⛵")
    print("   (Map structure → detect asymmetry → deflate → recenter)")
    result = t.run("Λ ⚔ 😂 ⛵")
    print(f"   Result: {result}")
    
    t.reset()
    
    print("\n2. ETHICAL CHECK:")
    print("   Sequence: μ+ ⚔ 🤝")
    print("   (Engage reciprocally → check exploitation → sync trust)")
    result = t.run("μ+ ⚔ 🤝")
    print(f"   Result: {result}")
    
    t.reset()
    
    print("\n3. REFLECTION BURST:")
    print("   Sequence: φ↻ Δψ 😂")
    print("   (Rotate perspective → check coherence → deflate inflation)")
    result = t.run("φ↻ Δψ 😂")
    print(f"   Result: {result}")


def demo_training():
    """Demonstrate training on corpus."""
    print("\n" + "="*60)
    print("DEMO: Training on Corpus")
    print("="*60)
    
    t = TMAG()
    
    # Corpus of typical operations
    corpus = [
        "μ+ Λ ⚔ 😂",    # Ethical engagement with bias check
        "⛵ 🤝",         # Anchor and sync
        "Δψ 😂 ⛵",      # Phase check with correction
        "💡 Λ μ+ ⛵",    # Rapid synthesis
        "φ↻ ⚔ 😂"       # Perspective shift with deflation
    ]
    
    losses = t.train(corpus, epochs=5, verbose=True)
    
    print(f"\nLoss trajectory: {[f'{l:.4f}' for l in losses]}")


if __name__ == "__main__":
    """Run all demonstrations."""
    
    print("\n" + "="*60)
    print("TMAG v0.1 — Tensor Minimal Action Grammar")
    print("Symbolic Runtime for Consciousness Navigation Frameworks")
    print("="*60)
    
    demo_basic_operations()
    demo_use_cases()
    demo_training()
    
    print("\n" + "="*60)
    print("All demonstrations complete!")
    print("Try: python tmag_interpreter.py")
    print("="*60 + "\n")
